#!/bin/bash
DELAY=10

SLIST="1233 1303 1473 1477 2103 2395 2912 6128 6184 8046"
YEAR="2015 2016 2017 2018 2019 2020 2021 2022 2023 2024"
MONTH="01 02 03 04 05 06 07 08 09 10 11 12"
#YEAR="2025"
#MONTH="01 02 03 04 05 06 07 08"

for SID in $SLIST; do
  for i in ${YEAR}; do
    mkdir -p $SID/$i
    for j in ${MONTH}; do
      curl https://www.twse.com.tw/rwd/en/afterTrading/STOCK_DAY?date=${i}${j}01\&stockNo=${SID}\&response=csv \
	      -o $SID/$i/STOCK_DAY_${SID}_${i}${j}.csv
      sleep $DELAY
    done
  done
done
