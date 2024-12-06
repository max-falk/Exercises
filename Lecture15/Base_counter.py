#!/usr/bin/env python3

#Q3 - Base counter

def base_counter(DNA, threshold=0.8):
	count=0
	for base in DNA :
		if base =='A' or base =='T' or base =='G' or base =='C':
			count=count
		else:
			count=count+1
	undetermined = count/len(DNA)
	if undetermined >= threshold :
		print('TRUE')
	else:
		print('FALSE')
