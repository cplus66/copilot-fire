#!/bin/bash
SID=2412
DELAY=10
YEAR="2015 2016 2017 2018 2019 2020 2021 2022 2023 2024"
MONTH="01 02 03 04 05 06 07 08 09 10 11 12"

#YEAR="2025"
#MONTH="01 02 03 04 05 06 07 08"

for i in ${YEAR}; do
    mkdir -p $i
    for j in ${MONTH}; do
      curl https://www.twse.com.tw/rwd/en/afterTrading/FMTQIK?date=${i}${j}01\&response=csv\
	      -o $i/FMTQIK_${i}${j}.csv
      sleep $DELAY
    done
done
