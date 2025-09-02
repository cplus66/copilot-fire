#!/bin/bash
#
# Prerequist:
#   sudo apt install -y parallel

# CONFIGURATION
KEY_NAME="ec2-2015-1005"
KEY_PATH="~/.ssh/aws_ec2-2015-1005.pem"
SECURITY_GROUP_ID="sg-0a7772b28bc917374"
INSTANCE_TYPE="t2.micro"
REGION="us-east-1"
UBUNTU_AMI="ami-020cba7c55df1f615"  # Ubuntu 24.04 LTS
EC2_USER=ubuntu

#
# Internal function
#

# 1. CREATE INSTANCE
_ec2_create() {
  COUNT=$1
  if [ -z $COUNT ]; then
    COUNT=1
  fi

  echo "Creating EC2 instance..."
  INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $UBUNTU_AMI \
    --count $COUNT \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $SECURITY_GROUP_ID \
    --region $REGION \
    --query 'Instances[0].InstanceId' \
    --output text)
  echo "Instance ID: $INSTANCE_ID"

  # 2. WAIT UNTIL RUNNING
  echo "Waiting for instance to be running..."
  aws ec2 wait instance-running --instance-ids $INSTANCE_ID --region $REGION

  # 3. GET PUBLIC IP
  PUBLIC_IP=$(aws ec2 describe-instances \
    --instance-ids $INSTANCE_ID \
    --region $REGION \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text)
  echo "Instance Public IP: $PUBLIC_IP"

  # export INSTANCE_ID and PUBLIC_IP
  export INSTANCE_ID
  export PUBLIC_IP

  # 4. WAIT FOR SSH TO BE READY
  #echo "Waiting for SSH to be ready..."
  #sleep 60
}


# 5. SSH AND RUN COMMAND
_ec2_connect() {
  echo "Connecting to EC2 $PUBLIC_IP ..."
  ssh -i $KEY_PATH -o StrictHostKeyChecking=no ${EC2_USER}@$PUBLIC_IP
}

_ec2_run() {
  echo "Run '$1' on EC2 $PUBLIC_IP ..."
  CMD="$*"
  ssh -i $KEY_PATH -o StrictHostKeyChecking=no ${EC2_USER}@$PUBLIC_IP "$CMD"
}

_ec2_upload() {
  echo "upload '$*' on EC2 $PUBLIC_IP ..."
  FILES="$*"
  scp -i $KEY_PATH -r "$FILES" ${EC2_USER}@$PUBLIC_IP:
}

# 6. TERMINATE INSTANCE
_ec2_terminate() {
  echo "Terminating instance..."
  aws ec2 terminate-instances --instance-ids $INSTANCE_ID --region $REGION

  echo "Waiting for termination..."
  aws ec2 wait instance-terminated --instance-ids $INSTANCE_ID --region $REGION

  echo "Instance terminated."
}

# mgmt
ec2_create() {
  COUNT=$1

  if [ -z $COUNT ]; then
    COUNT=1
  fi

  _ec2_create $COUNT
}

ec2_connect() {
  if [ -z $1 ]; then
    ID=0
  else
    ID=$1
  fi

  LIST=($(ec2_ip))
  if [ -z $LIST ]; then
    echo "No availabe instance"
  else
    PUBLIC_IP=${LIST[$ID]} _ec2_connect
  fi
}

ec2_run() {
  CMD="$*"
  LIST="$(ec2_ip)"
  for i in $LIST; do
    PUBLIC_IP=$i _ec2_run "$CMD"
  done
}

ec2_upload() {
  FILES=$*

  LIST="$(ec2_ip)"
  for i in $LIST; do
    PUBLIC_IP=$i _ec2_upload "$FILES"
  done
}

ec2_terminate() {
  LIST="$(ec2_id)"

  for i in $LIST; do
    INSTANCE_ID=$i _ec2_terminate
  done
}

ec2_ip() {
  aws ec2 describe-instances \
    --filters "Name=instance-state-name,Values=running" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text
}

ec2_id() {
  aws ec2 describe-instances \
    --query "Reservations[*].Instances[*].InstanceId" \
    --output text
}

ec2_setup() {
  # Ubuntu packages
  ec2_run sudo apt-get update
  ec2_run sudo apt-get install -y jq
  ec2_run sudo apt-get install -y tree

  # AWS CLI
  ec2_upload ~/.aws
  ec2_upload awscli_install.sh
  ec2_run ./awscli_install.sh

  # Bash library
  ec2_upload .profile
  ec2_upload lib
}

ec2_cleanup() {
  ec2_run rm -rf ~/awscli_install.sh
  ec2_run rm -rf ~/lib
  ec2_run rm -rf ~/.profile
}

ec2_progress() {
  ec2_run "source ./lib/lib.sh; progress"
}

# Generate parallel configuration
ec2_gen_conf() {
  IP_CONF="ip.txt"
  PARALLEL_CONF="config.json"

  cd parallel
  rm -f $IP_CONF
  LIST=$(ec2_ip)
  for i in $LIST; do echo $i >> $IP_CONF; done

  ./manage_instances.sh load-file ip.txt
  cat $PARALLEL_CONF
  cd ..
}

#
# Run in parallel 
#
ec2_parallel_run() {
  CMD="$*"
  instances=($(ec2_ip))

  parallel -j "$num_instances" ssh -i $KEY_PATH -o StrictHostKeyChecking=no ${EC2_USER}@{} "$CMD" ::: "${instances[@]}"
}

ec2_parallel_upload() {
  FILES=$*
  instances=($(ec2_ip))
  num_instances=${#instances[@]}

  parallel -j "$num_instances" scp -i $KEY_PATH -r "$FILES" ${EC2_USER}@{}: ::: "${instances[@]}"
}

ec2_parallel_setup() {
  FILES="~/.aws awscli_install.sh .profile lib ec2_setup.sh"
  instances=($(ec2_ip))
  num_instances=${#instances[@]}

  ec2_parallel_upload $FILES
  ec2_parallel_run ~/ec2_setup.sh
}

# Split data file and upload to remote host
ec2_parallel_split_and_upload() {
  CODE_FILE=$1
  DATA=$2
  DATA_DIR=$3
  CHUNK_PREFIX="chunk"

  if [ -z $CODE_FILE -o -z $DATA -o -z $DATA_DIR ]; then
    echo "Usage: $0 <data> <data_dir>"
    exit 1
  fi
  
  instances=($(ec2_ip))

  # Split data into chunks
  split -n l/${#instances[@]} -d "$DATA" "$DATA_DIR/$CHUNK_PREFIX"

  # Loop over instances and distribute data/code
  for i in "${!instances[@]}"; do
    CHUNK_FILE="${DATA_DIR}/${CHUNK_PREFIX}$(printf "%02d" $i)"
    INSTANCE="${instances[$i]}"

    # Copy code and data chunk
    scp -i $KEY_PATH "$CODE_FILE" "$CHUNK_FILE" ${EC2_USER}@$INSTANCE: > /dev/null
  done

}
