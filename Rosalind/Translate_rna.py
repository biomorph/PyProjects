__author__ = 'ravi'
import re

def translate (codon_fh,message):
    codon_dict = {}

    for line in codon_fh:
        codon = re.split(r'\t',line.strip())[0]
        amino_acid = re.split(r'\t',line.strip())[1]
        codon_dict[codon] = amino_acid
    #print len(codon_dict)
    codon_fh.close()



    i = 0
    protein = ""
    while i < len(message):
        codon = message[i:i+3]
        if(codon_dict[codon] != "Stop"): protein = protein + codon_dict[codon]
        i = i + 3

    print protein
    return

if __name__=='__main__':

    codon_fh = open("codon_table.txt",'rU')
    rna_fh = open("rosalind_prot.txt",'rU')
    rna = rna_fh.read().strip()
    translate(codon_fh,rna)





