__author__ = 'ravi'
from Bio.Seq import translate


translate_fh = open("rosalind_ptra.txt",'rU')

entry = translate_fh.readlines()

dna_seq = entry[0].strip()
protein_seq = entry[1].strip()

for codon_table in [1,2,3,4,5,6,9,10,11,12,13,14,15]:
    if translate(dna_seq,table=codon_table,stop_symbol='') == protein_seq:
       print codon_table
       break
#print dna_seq
#print protein_seq

translate_fh.close()
