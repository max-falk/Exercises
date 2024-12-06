#!/usr/bin/env python3

def percent_protein(protein, amino_acid) :
	protein_length = len(protein)
	amino_acid_count = protein.upper().count(amino_acid)
	percentage = (amino_acid_count * 100) / protein_length
	return percentage
 
#Now modifying for Q2
def percent_aa_2(protein, aa_list):
	protein_length = len(protein)
	counter = 0
	for aa in aa_list:
		aa_count=protein.upper().count(aa.upper())
		counter = counter + aa_count 
	percentage = (counter/len(protein)) * 100
	return percentage 

#NOTE - to get into python use syntax 'from (scriptname) import (functionname)
#e.g. from AA_percent import percent_aa_2 
#Then can input arguments as you need 

