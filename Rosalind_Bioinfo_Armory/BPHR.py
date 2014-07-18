__author__ = 'ravi'
from Bio import SeqIO
from numpy import *


fastq_fh = open("rosalind_bphr.txt",'rU')

quality_threshold = fastq_fh.readline().strip()
fastq_records = list(SeqIO.parse(fastq_fh,"fastq"))

read_number = len(fastq_records)
read_length = len(fastq_records[0].seq)

quality_array = empty(shape=(read_length,read_number))
record_num = 0

for fastq in fastq_records:
    quality_array[:,record_num] = fastq.letter_annotations.values()[0]
    record_num = record_num + 1

avg_quality_array = quality_array.mean(axis=1)

print len(avg_quality_array [avg_quality_array < int(quality_threshold)])





