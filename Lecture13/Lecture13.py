#!/usr/bin/env python3

import os

#Exercise1
#First, trimming the adaptor sequence 
with open("input.txt", "r") as infile, open("noadaptor.txt", "w") as outfile:
	for sequence in infile:
		no_adaptor = sequence[14:]
		outfile.write(no_adaptor + " " + str(len(no_adaptor)) + "\n")

#Exercise2
with open("genomic_dna2.txt", "r") as file, open("exons_only.txt", "w") as outfile:
	file = file.read()
	outfile.write(file[4:58] + file[71:133] + file[189:276] + file[339:398])

#Exercise3
#Sliding window creation
sequence = open("noheading.fasta").read().rstrip()
windowsize = 30
offset = 3
segment_starts = list(range(0, len(sequence) - windowsize + 1, offset))

#Opening a file 
with open ("window_segments", "w") as allsegments:
#Creating a dictionary 
	segments_made = []
#Managing the for loop
	for seg_bits in segment_starts:
		tempseq = sequence[seg_bits:seg_bits + windowsize].upper()
		segments_made = segments_made + [tempseq]
		allsegments.write(tempseq + "\n")

