#!/usr/bin/env python3

#Print kmers occuring more than n number of times 
sequence = input("What is the sequence ").upper()
n = int(input("chunk length?"))
x = int(input("Min number of times kmer appear?"))

#Extracting out the chunks
chunks = []
for i in range(0, len(sequence), n):
	chunks.append(sequence[i:i+n])

#Now need to count them all
unique_chunks = set(chunks)
for chunk in unique_chunks:
	count = chunks.count(chunk)
	if count > x:
		print(f"{chunk}:{count}")


