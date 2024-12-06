#!/usr/bin/env python3



DNA = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

for i in range(len(DNA)):
	for j in range(i+1, len(DNA)):
		seq1 = DNA[i]
		seq2 = DNA[j]
		count=0
		for k in range(len(seq1)):
			base1 = seq1[k]
			base2 = seq2[k]
			if base1 == base2:
				count=count+1
			else:
				count = count
		percent = int((count/len(seq1)*100))
		print(f"% similarity for {seq1} + {seq2} = {percent}")
