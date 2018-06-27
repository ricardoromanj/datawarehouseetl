#!/usr/bin/bash

# cat $1 | awk ''

let a=0
MONTHS=(JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC)

# while [ $a -le 25 ]
while read row
do
  let num=($a % 12)
  # echo "Month ${MONTHS[num]}"
  echo "${MONTHS[num]},${row}"
  let a++
done < ./sample.csv
