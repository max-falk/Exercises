#!/usr/bin/env python3

def percent_protein(protein, amino_acid) :
	protein_length = len(protein)
	amino_acid_count = protein.upper().count(amino_acid)
	percentage = (amino_acid_count * 100) / protein_length
	return percentage
