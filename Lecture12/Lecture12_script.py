#!/usr/bin/env python3

import os
import shutil
import subprocess


# Reading the files into variables
with open("noheading.fasta", "r") as file:
    noheading_fasta = file.read()

with open("relevant_sequence.txt", "r") as file:
    relevant_sequence_txt  = file.read()

#Splitting the genomic DNA into coding and non-coding parts

remote_noncoding01 = noheading_fasta[0:28]
remote_exon01 = noheading_fasta[28:409]
remote_noncoding02 = noheading_fasta[409:]

local_exon01 = relevant_sequence_txt[0:63]
local_intron01 = relevant_sequence_txt[63:90]
local_exon02 = relevant_sequence_txt[90:]

#Concatonating the local_exons into one
local_coding = local_exon01 + local_exon02
remote_coding = remote_exon01

#Writing to files 
with open("coding_sequences", "w") as file:
	file.write("Local Coding Sequence is " + local_coding);
	file.write("\n" + "Remote Coding Sequence is " + remote_coding)
 


