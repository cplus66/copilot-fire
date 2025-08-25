
#!/bin/bash

CONFIG_FILE="config.json"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: $CONFIG_FILE not found."
  exit 1
fi

COMMAND=$1
ARG=$2

if [ -z "$COMMAND" ]; then
  echo "Usage: $0 [add|remove|remove-all|list|load-file] [argument]"
  exit 1
fi

if [ "$COMMAND" == "add" ]; then
  if [ -z "$ARG" ]; then
    echo "Instance address required for 'add'."
    exit 1
  fi
  jq --arg inst "$ARG" 'if .INSTANCES | index($inst) then . else .INSTANCES += [$inst] end' "$CONFIG_FILE" > tmp.json && mv tmp.json "$CONFIG_FILE"
  echo "Instance $ARG added."
elif [ "$COMMAND" == "remove" ]; then
  if [ -z "$ARG" ]; then
    echo "Instance address required for 'remove'."
    exit 1
  fi
  jq --arg inst "$ARG" '.INSTANCES -= [$inst]' "$CONFIG_FILE" > tmp.json && mv tmp.json "$CONFIG_FILE"
  echo "Instance $ARG removed."
elif [ "$COMMAND" == "remove-all" ]; then
  jq '.INSTANCES = []' "$CONFIG_FILE" > tmp.json && mv tmp.json "$CONFIG_FILE"
  echo "All instances removed."
elif [ "$COMMAND" == "list" ]; then
  echo "Current EC2 Instances:"
  jq -r '.INSTANCES[]' "$CONFIG_FILE"
elif [ "$COMMAND" == "load-file" ]; then
  if [ ! -f "$ARG" ]; then
    echo "Error: File $ARG not found."
    exit 1
  fi
  jq --argjson new_instances "$(jq -R . < $ARG | jq -s .)" '.INSTANCES = $new_instances' "$CONFIG_FILE" > tmp.json && mv tmp.json "$CONFIG_FILE"
  echo "Instances loaded from $ARG."
else
  echo "Invalid command. Use 'add', 'remove', 'remove-all', 'list', or 'load-file'."
  exit 1
fi
