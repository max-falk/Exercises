#!/bin/bash

IFS=$'\t'
count=0
while read name email city birthday_day birthday_month birthday_year country
do
if test -z ${name}
then 
echo -e "X\tblank line found"
else
if test ${country} == "country"
then
echo -e "X\tHeader line found"
else
count=$((count+1))
echo -e "${count}\t${name}\t${city}\t${country}"
fi
fi
done < example_people_data.tsv


count=0
IFS=$'\t'
while read name email city birthday_day birthday_month birthday_year country
do
if test -z ${name} || test ${country} == "country"
then 
echo "Ignoring"
else
count=$((count+1));
echo -e "${count}\t${name}\t{city}\t${country}" >> ${country// /}.details

fi
done < example_people_data.tsv
