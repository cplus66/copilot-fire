#!/bin/bash
source ../lib.sh

LIST=$(cat ../index_date.csv)
PREFIX="https://www.twse.com.tw/rwd/en/afterTrading/BFIAMU?date="

for i in $LIST; do
  url="${PREFIX}${i}\&response=csv"
  file="BFIAMU_${i}.csv"
  download_csv $url $file
done
