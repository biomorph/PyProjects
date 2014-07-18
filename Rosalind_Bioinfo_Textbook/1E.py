__author__ = 'ravi'
import re
input_fh = open("rosalind_1e.txt",'rU')

genome = input_fh.readline().strip()

skew_dict = {}
running_C_count = 0
running_G_count = 0

for i in range(0,len(genome)+1):
    prefix = genome[i:i+1]
    skew = running_G_count-running_C_count
    if prefix == "C": running_C_count = running_C_count + 1
    if prefix == "G": running_G_count = running_G_count + 1
    if skew in skew_dict.keys(): skew_dict[skew].append(i)
    else: skew_dict[skew] = [i]

min_skews = skew_dict[sorted(skew_dict.keys())[0]]
print " ".join(map(str,min_skews))
