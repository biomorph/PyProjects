__author__ = 'ravi'

dna_fh = open('rosalind_revC.txt', 'rU')


dna_string = dna_fh.read()
dna_fh.close()

def revC (dna_string):
    dna_revC_string = ""
    for base in dna_string:
        if base == "A": dna_revC_string = "T" + dna_revC_string
        if base == "T": dna_revC_string = "A" + dna_revC_string
        if base == "G": dna_revC_string = "C" + dna_revC_string
        if base == "C": dna_revC_string = "G" + dna_revC_string
    return dna_revC_string

#print revC(dna_string)