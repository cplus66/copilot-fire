#!/bin/bash 

for ((i=0; i<100; i++)); do
  echo "BEGIN",$i,"END" >> your_data.csv
done
