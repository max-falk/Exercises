#!/usr/bin/env python3
#Program to caculate A+T content 
#Written by s2759112 on 30/11
#----------------------------------#

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count = my_dna.upper().count("A")
T_count = my_dna.upper().count("T")

A_T_Content = (A_count + T_count) / len(my_dna)

print("A+T content is " + str(A_T_Content))


#Program to print complement of the DNA
dna_new = my_dna.replace("A", "t")
dna_new = dna_new.replace("T", "a")
dna_new = dna_new.replace("G", "c")
dna_new = dna_new.replace("C", "g")

print("Reverse complement is " + dna_new.upper())

#Restriction fragment lengths 
#First, finding position of motif 
my_dna_2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
location = my_dna_2.find("GAATTC")
print(location)
#Now figure out position of the cut 
cut = location + 1
#Second fragment 
fragment_2 = len(my_dna_2) - cut

print("Length of fragment 1 is " + str(cut) + " . Length of fragment 2 is " + str(fragment_2))



#Splicing out introns 
my_dna_3 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = my_dna_3[0:63]
exon_2 = my_dna_3[90:]
spliced_dna = exon_1 + exon_2
print("The spliced exons have the sequence " + str(spliced_dna))
