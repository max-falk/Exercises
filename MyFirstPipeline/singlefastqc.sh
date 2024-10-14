#!/bin/bash

READ1="./sequence_data/Tco-106_1.fq.gz"
READ2="./sequence_data/Tco-106_2.fq.gz"

OUT_DIR="./qc.results"

mkdir -p $OUT_DIR

fastqc -t 2 -o $OUT_DIR $READ1 $READ2
