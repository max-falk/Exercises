#!/usr/bin/env python3

import re

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

for accession in accessions: 
    if re.search('5', accession):
       print(accession + ' contains the number 5')
    else: 
       print(accession + ' doesnt contain 5')

    if re.search('d', accession) or re.search('e', accession): 
       print(accession + ' contains the letter d or e')
    else:
       print(accession + ' doesnt contain letter d or e')

    if re.search('de', accession):
       print(accession + ' contains de')
    else:
       print(accession + ' doesnt contain de')


#NOTE, \d indicates digits 
# \D = non-digit 
# \w = alphanumeric 
#Remember to include r before string to indicate raw string 







