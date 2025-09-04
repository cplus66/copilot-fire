#!/bin/bash 
# https://emops.twse.com.tw/server-java/t05st09_2_e?step=show&year=2024

PREFIX="https://emops.twse.com.tw/server-java/t05st09_2_e?step=show&year="

for i in $(seq 2015 2025); do
  curl ${PREFIX}$i -o t05st09_2_e_$i.html
done
