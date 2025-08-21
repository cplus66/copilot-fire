#!/bin/bash
source ../lib.sh

LIST=$(cat ../index_date.csv)
PREFIX="https://www.twse.com.tw/rwd/en/afterTrading/BWIBBU_d?date="

for i in $LIST; do
  url="${PREFIX}${i}&selectType=ALL&response=csv"
  file="BWIBBU_d_ALL_${i}.csv"
  download_csv $url $file
done
