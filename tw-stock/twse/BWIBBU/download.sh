#!/bin/bash
DELAY=10
PREFIX="https://www.twse.com.tw/rwd/en/afterTrading/BFIAMU?date="
PREFIX=" https://www.twse.com.tw/rwd/en/afterTrading/BWIBBU_d?date="

download_csv() {
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

LIST=$(cat ../index_date.csv)

for i in $LIST; do
  url="${PREFIX}${i}&selectType=ALL&response=csv"
  file="BWIBBU_d_ALL_${i}.csv"
  download_csv $url $file
done
