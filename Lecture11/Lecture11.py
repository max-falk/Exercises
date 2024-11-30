#!/usr/bin/env python3

#Q1
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
T_count = sequence.count("T")
print(T_count)
A_count = sequence.count("A")
print(A_count)
AT_proportion = (T_count + A_count) / len(sequence)
print(AT_proportion)

#Q2
sequence_complement = (sequence.replace("A", "T")
sequence_complement2 = (sequence_complement.replace("T", "A"))
sequence_complement3 = (sequence_complement2.replace("C", "G"))
sequence_complement4 = (sequence_complement3.replace("G", "C"))
 
print(sequence_complement4)

 
