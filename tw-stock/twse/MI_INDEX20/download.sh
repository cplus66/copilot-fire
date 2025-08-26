#!/bin/bash -xe

PREFIX="https://www.twse.com.tw/rwd/en/afterTrading/MI_INDEX20?date="
POSTFIX="\&response=csv"

INDEX="../index_date.csv"
for i in $(cat $INDEX); do
  echo download ${PREFIX}${i}${POSTFIX} MI_INDEX20/MI_INDEX20_${i}.csv
done
