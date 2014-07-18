__author__ = 'ravi'
import re

dna_fh = open('rosalind_rna.txt', 'rU')

dna_string = dna_fh.read()

print re.sub(r'T','U',dna_string)
