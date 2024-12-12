#!/usr/bin/env python3 

import re

index=[]
length=[]

with open('long_dna.txt', 'r') as infile: 
	dna_sequence = infile.read()



print("Length of sequence is " + str(len(dna_sequence)))

for site in re.finditer('A[ATCG]TAAT', dna_sequence):
	index.append(site.start())


#Trying (unsuccessfully) here to take all indicesfrom list  and calculate lengths 
#Wasn't quite sure how to do last fragment this way. Needs revisiting.....
for i in range(1, len(index)):
	length.append(index[i] - index[i-1])
	last_match = index[-1]
	length.append(len(dna_sequence) - last_match)

print("Lengths of fragments:", length)
