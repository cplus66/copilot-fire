#!/bin/bash
DELAY=10

SLIST="1233 1303 1473 1477 2103 2395 2912 6128 6184 8046"
SLIST="2330"

start_year=2015
start_month=1
end_year=2025
end_month=8

year=$start_year
month=$start_month

for SID in $SLIST; do
  while [ $year -lt $end_year ] || { [ $year -eq $end_year ] && [ $month -le $end_month ]; }; do
    y=$(printf %04d $year)
    m=$(printf %02d $month)

    mkdir -p $SID/$y
    curl https://www.twse.com.tw/rwd/en/afterTrading/STOCK_DAY?date=${y}${m}01\&stockNo=${SID}\&response=csv \
	      -o $SID/$y/STOCK_DAY_${SID}_${y}${m}.csv
    sleep $DELAY

    month=$((month + 1))
    if [ $month -gt 12 ]; then
      month=1
      year=$((year + 1))
    fi
  done
done
