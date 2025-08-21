download_csv() {
  DELAY=10
  url=$1
  file=$2

  while true; do
    curl $url -o $file
    sleep $DELAY

    if [ -f $file ]; then
      size=$(wc -c < $file)
      if [ "$size" -gt 500 ]; then
        break
      fi
    fi
  done
}

