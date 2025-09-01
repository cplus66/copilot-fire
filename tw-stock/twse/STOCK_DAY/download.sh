#!/bin/bash
#
# Resolve the path to the project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Load shared bash library
source "$PROJECT_ROOT/lib/utils.sh"

DELAY=10

SLIST="1233 1303 1473 1477 2103 2395 2912 6128 6184 8046"
SLIST="1101"

start_year=2015
start_month=1
end_year=2025
end_month=7

year=$start_year
month=$start_month

for SID in $SLIST; do
  while [ $year -lt $end_year ] || { [ $year -eq $end_year ] && [ $month -le $end_month ]; }; do
    y=$(printf %04d $year)
    m=$(printf %02d $month)

    mkdir -p $SID/$y
    while true; do
       file="$SID/$y/STOCK_DAY_${SID}_${y}${m}.csv"
       curl https://www.twse.com.tw/rwd/en/afterTrading/STOCK_DAY?date=${y}${m}01\&stockNo=${SID}\&response=csv \
	      -o $file
       sleep $DELAY
       size=$(wc -c < $file)
       if [ "$size" -gt 500 ]; then
         break
       fi
    done

    month=$((month + 1))
    if [ $month -gt 12 ]; then
      month=1
      year=$((year + 1))
    fi
  done
done
