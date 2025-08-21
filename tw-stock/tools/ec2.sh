#!/bin/bash

# CONFIGURATION
KEY_NAME="ec2-2015-1005"
KEY_PATH="~/.ssh/aws_ec2-2015-1005.pem"
SECURITY_GROUP_ID="sg-0a7772b28bc917374"
INSTANCE_TYPE="t2.micro"
REGION="us-east-1"
UBUNTU_AMI="ami-020cba7c55df1f615"  # Ubuntu 24.04 LTS

# 1. CREATE INSTANCE
ec2_create() {
  echo "Creating EC2 instance..."
  INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $UBUNTU_AMI \
    --count 1 \
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
  echo "Waiting for SSH to be ready..."
  sleep 60
}

# 5. SSH AND RUN COMMAND
_ec2_connect() {
  echo "Connecting to EC2 $PUBLIC_IP ..."
  ssh -i $KEY_PATH -o StrictHostKeyChecking=no ubuntu@$PUBLIC_IP
}

_ec2_run() {
  echo "Run '$1' on EC2 $PUBLIC_IP ..."
  CMD="$*"
  ssh -i $KEY_PATH -o StrictHostKeyChecking=no ubuntu@$PUBLIC_IP "$CMD"
}

_ec2_upload() {
  echo "upload '$*' on EC2 $PUBLIC_IP ..."
  FILES="$*"
  scp -i $KEY_PATH -r "$FILES" ubuntu@$PUBLIC_IP:
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

ec2_terminate() {
  LIST="$(ec2_id)"

  for i in $LIST; do
    INSTANCE_ID=$i _ec2_terminate
  done
}

ec2_connect() {
  if [ x$1 == "x" ]; then
    ITEM=0
  fi

  LIST=($(ec2_ip))
  if [ x$LIST != "x" ]; then
    PUBLIC_IP=${LIST[$1]} _ec2_connect
  else
    echo "No availabe instance"
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

ec2_setup() {
  ec2_upload ~/.aws
  ec2_upload awscli_install.sh
  ec2_run ./awscli_install.sh
  ec2_run rm -rf ~/awscli_install.sh
}

ec2_cleanup() {
  ec2_run rm -rf ~/awscli_install.sh
}

