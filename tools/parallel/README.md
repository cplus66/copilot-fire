# Parallel Run Framework

1. Split job into code (process.sh) and data(data_all.txt). The data as default parameter of code.
1. Config the config.json for multiple instances.
1. Run "parallel.sh".

## Configuration(config.json)
```
{
  "INSTANCES": [
    "ubuntu@ec2-0",
    "ubuntu@ec2-1",
    "ubuntu@ec2-2"
  ],
  "CODE_FILE": "process.sh",
  "DATA": "data_all.txt",
  "DATA_DIR": "./data",
  "CREDENTIAL": "~/.ssh/id_rsa_aws_ec2"
}
```

## Instances (EC2) Management on Configuration (config.json)

```
Usage: ./manage_instances.sh [add|remove|remove-all|list|load-file] [argument]

Example: 
Load instances(ip.txt) into config.json
$ ./manage_instances.sh load-file ip.txt

List all instances
$ ./manage_instances.sh list

```

