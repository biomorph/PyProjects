__author__ = 'ravi'
import re

input_fh = open("rosalind_1d.txt",'rU')
genome = input_fh.readline().strip()
k, L, t = map(int, input_fh.readline().split())
kmer_dict = {}
kmer_clump_list = []


for i in range(0,len(genome)-k+1):
    current_kmer = genome[i:i+k]
    if current_kmer in kmer_dict: kmer_dict[current_kmer] = kmer_dict[current_kmer] + 1
    else: kmer_dict[current_kmer] = 1


for kmer in kmer_dict.keys():
    if kmer_dict[kmer] >= t:
        print kmer, kmer_dict[kmer]
        regex = re.compile('(?=%s)'%kmer)
        matches = re.finditer(regex,genome)
        match_starts = []
        for match in matches:
            match_starts.append(match.start(0))
        print max(match_starts) - min(match_starts)
        for i in range(0,len(match_starts)-t + 1):
            window = match_starts[i:i+t]
            if window[-1] - window[0] <= L and kmer not in kmer_clump_list:
                kmer_clump_list.append(kmer)

print " ".join(kmer_clump_list)

