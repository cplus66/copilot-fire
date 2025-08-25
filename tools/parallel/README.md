# Parallel Run Framework

1. Split job into code (process.sh) and data(data_all.csv). The data as default parameter of code.
1. Config the config.json for multiple instances.
1. Run "parallel.sh".

## Configuration(config.json)
```
{
  "INSTANCES": [
    "jetpack-0",
    "jetpack-1",
    "jetpack-2"
  ],
  "CODE_FILE": "process.sh",
  "DATA": "data_all.csv",
  "DATA_DIR": "./data",
  "CREDENTIAL": "~/.ssh/id_rsa_gw"
}
```

## Instances (EC2) Management on Configuration (config.json)

```
Usage: ./manage_instances.sh [add|remove|remove-all|list|load-file] [argument]
Example: 
  Load instances(ip.txt) into config.json
  ./manage_instances.sh load-file ip.txt

  List all instances
  ./manage_instances.sh list

```

