#!/bin/bash -x

# Definition
OUTPUT_FOLDER=output
timestamp=$(date '+%Y-%m-%d-%H-%M')
hostname=$(hostname)
upload_file=${hostname}_${timestamp}.tgz

# include library
source ~/lib/lib.sh

# Path to your command file
COMMAND_FILE=$1

# Check if the file exists
if [[ ! -f "$COMMAND_FILE" ]]; then
  log "Command file not found: $COMMAND_FILE"
  exit 1
fi

# Read and execute each line
while IFS= read -r cmd || [[ -n "$cmd" ]]; do
  log "Running: $cmd"
  eval "$cmd"
  log "Sleeping for 10 seconds..."
  sleep 10
done < "$COMMAND_FILE"

# Upload file to S3
tar -C $OUTPUT_FOLDER -czvf $upload_file .
aws s3 cp $upload_file s3://prjdoc/upload/
