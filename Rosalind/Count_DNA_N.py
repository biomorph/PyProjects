__author__ = 'ravi'
import sys
import re

dna_fh = open('/Users/ravi/PycharmProjects/Rosalind/rosalind_dna.txt', 'rU')

dna_string = dna_fh.read()
dna_fh.close()
num_A = len(re.findall(r'A',dna_string))
num_C = len(re.findall(r'C',dna_string))
num_G = len(re.findall(r'G',dna_string))
num_T = len(re.findall(r'T',dna_string))

print "%d %d %d %d" %(num_A,num_C,num_G,num_T)


