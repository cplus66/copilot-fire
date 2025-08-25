#!/bin/bash -x

for i in $(cat $1); do
  echo -n "."
  sleep 1
done
