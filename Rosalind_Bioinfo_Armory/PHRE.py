__author__ = 'ravi'
from Bio import SeqIO
from numpy import mean

fastq_fh = open("rosalind_phre.txt",'rU')

fastq_records = SeqIO.parse(fastq_fh,"fastq")

phred_cutoff = fastq_fh.readline().strip()
print phred_cutoff
num_of_bad_reads = 0
for record in fastq_records:
    if mean(record.letter_annotations.values()) < int(phred_cutoff):
        num_of_bad_reads = num_of_bad_reads + 1
print num_of_bad_reads


