#!/usr/bin/env python3

genedata = open("data.csv").readlines()

#Q1 - printing gene names 
for geneline in genedata :
	gene_info = geneline.split(",")
	species = gene_info[0]
	gene_seq = gene_info[1].upper()
	seqlengths = len(gene_info[1])
	genenames = gene_info[2]
	expressionlevel = int(gene_info[3])	
	atcontent = (gene_seq.count('A') + gene_seq.count('T'))/seqlengths

	if "melanogaster" in species or "simulans" in species :
		print(species, genenames)
	else : 
		print("Not the right species ", genenames)

#Q2 - printing for 90-110 bases long 
	if len(genenames) <= 110 and len(genenames) >= 90 :
		print(genenames + " is between 90 and 100 bases" + "\n")

#Q3 - printing when AT content less than 0.5 + expression > 200
	if atcontent < 0.5 and expressionlevel > 200 :
		print(genenames + " satisfy conditions for Q3" + "\n")

#Q4 - genes beginning with "k" or "h"
	if (genenames.startswith("k") or genenames.startswith("h")) and species !=  "Drosophila melanogaster" :
		print(genenames + " satisfy conditions for Q4" + "\n")

#Q5 - 
	if atcontent > 0.65 :
		print(genenames + " AT content is HIGH")

	elif atcontent < 0.45 :
		print(genenames + " AT content is LOW")

	else:
		 print(genenames + " AT content is MEDIUM")
	




