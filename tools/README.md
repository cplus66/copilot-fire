# Tools for EC2 and Parallel

## Usage
Source the ec2.sh

```
$ source ./ec2.sh
```

```
Create EC2 instances
$ ec2_create <number>

Terminate EC2 instances
$ ec2_terminate

List all EC2 instances
$ ec2_id

List all EC2 IPs 
$ ec2_ip

Connect EC2 instance (0..n-1)
$ ec2_connect <id>

Upload files to all EC2 instances
$ ec2_upload <file>

Setup EC2 environment on all EC2 instances
$ ec2_setup

Run command on all EC2 instances
$ ec2_run <cmds*>

Clean up on all EC2 instances
$ ec2_cleanup

```

## Configuration

```
# CONFIGURATION
KEY_NAME="ec2-2015-1005"
KEY_PATH="~/.ssh/aws_ec2-2015-1005.pem"
SECURITY_GROUP_ID="sg-0a7772b28bc917374"
INSTANCE_TYPE="t2.micro"
REGION="us-east-1"
UBUNTU_AMI="ami-020cba7c55df1f615"  # Ubuntu 24.04 LTS
```
