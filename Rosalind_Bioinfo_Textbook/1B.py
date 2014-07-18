__author__ = 'ravi'

import sys
input_fh = open("rosalind_1b.txt",'rU')

dna_string = input_fh.readline().strip()

base_dict = {}

base_dict ["A"] = "T"
base_dict ["T"] = "A"
base_dict ["G"] = "C"
base_dict ["C"] = "G"

for i in range(1,len(dna_string)+1):
    sys.stdout.write(base_dict[dna_string[-i]])
