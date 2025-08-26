#!/bin/bash -x

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
