__author__ = 'ravi'
import Reverse_Comp
import re
def get_codon_dict(codon_fh):
    codon_dict = {}

    for line in codon_fh:
        codon = re.split(r'\t',line.strip())[0]
        amino_acid = re.split(r'\t',line.strip())[1]
        codon_dict[codon] = amino_acid
    codon_fh.close()
    return codon_dict

fasta_fh = open("rosalind_orf.txt",'rU')
codon_fh = open("codon_table_DNA.txt",'rU')
sequence = ""
for line in fasta_fh:
    if line.find(">") == -1: sequence = sequence + line.strip()
revC_sequence = Reverse_Comp.revC(sequence)

codon_dict = get_codon_dict(codon_fh)
fasta_fh.close()
codon_fh.close()

orf_proteins = []
for dna_string in [sequence, revC_sequence]:
    ATG_matches = re.finditer(r'ATG',dna_string)
    for match in ATG_matches:
        protein = ""
        i = match.start()
        while i < len(dna_string)-3:
            amino_acid = codon_dict[dna_string[i:i+3]]
            if amino_acid == "Stop":
                if protein not in orf_proteins: orf_proteins.append(protein)
                break
            else: protein = protein + amino_acid
            i = i + 3

for protein in orf_proteins: print protein



