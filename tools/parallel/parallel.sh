#!/bin/bash -e

# Load config file
CONFIG_FILE="config.json"
CHUNK_PREFIX="chunk"

# Define your EC2 instances
# Read values using jq
INSTANCES=($(jq -r '.INSTANCES[]' "$CONFIG_FILE"))
CODE_FILE=$(jq -r '.CODE_FILE' "$CONFIG_FILE")
DATA_DIR=$(jq -r '.DATA_DIR' "$CONFIG_FILE")
DATA=$(jq -r '.DATA' "$CONFIG_FILE")
CREDENTIAL=$(jq -r '.CREDENTIAL' "$CONFIG_FILE")

# Trap SIGINT (CTRL+C)
cleanup() {
    echo "Caught CTRL+C! Killing background jobs..."
    pkill -P $$  # Kill all child processes of this script
    exit 1
}
trap cleanup SIGINT

# Split data into chunks
split -n ${#INSTANCES[@]} -d "$DATA" "$DATA_DIR/$CHUNK_PREFIX"

# Loop over instances and distribute data/code
for i in "${!INSTANCES[@]}"; do
    CHUNK_FILE="${DATA_DIR}/${CHUNK_PREFIX}$(printf "%02d" $i)"
    INSTANCE="${INSTANCES[$i]}"

    # Copy code and data chunk
    scp -i $CREDENTIAL "$CODE_FILE" "$CHUNK_FILE" "$INSTANCE:~/" > /dev/null

    # Run code remotely in background
    ssh -i $CREDENTIAL "$INSTANCE" "bash ~/process.sh ~/$(basename $CHUNK_FILE)" &
done

# Wait for all background jobs to finish
wait
echo "All jobs completed."
