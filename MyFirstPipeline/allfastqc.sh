#!/bin/bash

INPUT_DIR="./sequence_data"  
OUT_DIR="./qc_results2"

mkdir -p $OUT_DIR

for READ1 in $INPUT_DIR/*_1.fq.gz ; do

READ2="${READ1/_1/_2}"

fastqc -t 2 -o $OUT_DIR $READ1 $READ2

done

