__author__ = 'ravi'
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC

fasta_fh = open("rosalind_rvco.txt", 'rU')

sequences = list(SeqIO.parse(fasta_fh,"fasta",alphabet=IUPAC.unambiguous_dna))

count = 0
for sequence in sequences:
    #print sequence.seq
    #print sequence.reverse_complement().seq
    if str(sequence.seq) == str(sequence.reverse_complement().seq):
        count = count + 1

print count
