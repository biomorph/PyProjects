__author__ = 'ravi'
import re

def get_codon_dict(codon_fh):
    codon_dict = {}
    for line in codon_fh:
        codon = re.split(r'\t',line.strip())[0]
        amino_acid = re.split(r'\t',line.strip())[1]
        if amino_acid not in codon_dict.keys():
            codon_dict[amino_acid] = [codon]
        else:
            codon_dict[amino_acid].append(codon)
    return codon_dict

codon_dict = get_codon_dict(open("codon_table.txt",'rU'))

protein_fh = open("rosalind_mRNA.txt",'rU')

protein_seq = protein_fh.read().strip()

combinations = 1
for amino_acid in protein_seq:
    combinations = (combinations * len(codon_dict[amino_acid]))%1000000
print combinations * len(codon_dict["Stop"])%1000000


