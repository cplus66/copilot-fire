#!/bin/bash 

# Download file with minimun file size 500 bytes and retry.
# 
# url: URL location
# file: destination file
# return: 
#   0: OK
#   1: NOK

download() {
  DELAY=10
  RETRY=3

  url=$1
  file=$2
  dir=$(dirname $file)

  if [ "x$dir" != "x." ]; then
    mkdir -p $dir
  fi

  for ((i=0; i<$RETRY; i++)); do
    curl $url -o $file
    sleep $DELAY

    if [ -f $file ]; then
      size=$(wc -c < $file)
      if [ "$size" -gt 500 ]; then
	return 0
      fi
    fi
  done
  return 1
}

# Logger function with timestamp and hostname
log() {
  local timestamp
  timestamp=$(date '+%Y-%m-%d %H:%M:%S')
  local hostname
  hostname=$(hostname)
  echo "[$timestamp][$hostname] $1"
}

progress() {
 T=$(wc chunk* | awk '{print $1'})
 N=$(ls output/* | wc | awk '{print $1'})
 python3 -c "a=$N;b=$T;print(f'{a/b:.1%}')"
}
