__author__ = 'ravi'

import Overlap_graph
import re
fasta_fh = open("rosalind_long.txt",'rU')

fasta_list = Overlap_graph.get_fasta_dict(fasta_fh).values()

first_sequence = ""
last_sequence = ""

for seq1 in fasta_list:
    count1, count2  = 0, 0
    for seq2 in fasta_list:
        if seq1 != seq2 and seq2.find(seq1[:len(seq1)/2])==-1:count1 = count1 + 1
        if seq1 != seq2 and seq2.find(seq1[len(seq1)/2:])==-1:count2 = count2 + 1
    if count1 == len(fasta_list)-1: first_sequence = seq1
    if count2 == len(fasta_list)-1: last_sequence = seq1
#print first_sequence
#print last_sequence

i = 0
fasta_list.remove(first_sequence)
fasta_list.remove(last_sequence)
fasta_list.append(last_sequence)

while i < len(fasta_list):
    second_seq = "".join([x for x in fasta_list if x.find(first_sequence[len(first_sequence)/2:])!=-1])
    print second_seq
    j = 0
    while True:
        if second_seq.find(first_sequence[-j+len(first_sequence)/2:]) == -1:
            first_sequence = first_sequence + second_seq[second_seq.find(first_sequence[-j+len(first_sequence)/2:])+j + len(first_sequence)/2:]
            print first_sequence
            print second_seq[second_seq.find(first_sequence[-j+len(first_sequence)/2:]):]
            break
        j = j + 1
    i = i + 1
#print first_sequence


'''
while i < len(first_sequence)/2:
    for seq in fasta_list:
        if seq.find(first_sequence[-i + len(first_sequence)/2:])==-1:
            first_sequence = first_sequence + seq[-i + 1 + len(first_sequence)/2:]
            fasta_list.remove(seq)
            break
        else: i = i + 1
print first_sequence
'''