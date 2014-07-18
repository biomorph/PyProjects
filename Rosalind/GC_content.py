#from __future__ import division
__author__ = 'ravi'
import re
fasta_fh = open('rosalind_gc.txt', 'rU')

fasta_dict = {}
fasta_heading = ""
sequence = ""
for line in fasta_fh:
    if re.search(r'^>',line):
        sequence = ""
        fasta_heading = line.strip().replace(">","")
        new = 1
    else: sequence = sequence + line.strip()
    fasta_dict[fasta_heading] = sequence
print fasta_dict

gc_list = []
for id in fasta_dict.keys():
    num_GC = float(len(re.findall(r'[GC]',fasta_dict[id])))
    percent_GC = 100*num_GC/len(fasta_dict[id])
    gc_list.append((percent_GC,id))

sorted_gc = sorted(gc_list,reverse=True)
print sorted_gc[0][1]
print sorted_gc[0][0]