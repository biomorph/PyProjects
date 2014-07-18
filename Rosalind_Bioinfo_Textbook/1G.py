__author__ = 'ravi'
import itertools
input_fh = open("rosalind_1g.txt",'rU')

text = input_fh.readline().strip()

kmer_size, d = map(int,input_fh.readline().split())

genome_size = len(text)

kmer_array=[]
mutated_kmer_array=[]
kmer_dict = {}




def mismatch(word, letters, num_mismatches):
    for locs in itertools.combinations(range(len(word)), num_mismatches):
        this_word = [char for char in word]
        print this_word
        for loc in locs:
            orig_char = word[loc]
            this_word[loc] = [l for l in letters if l != orig_char]
        print this_word
        for poss in itertools.product(*this_word):
            yield ''.join(poss)

for i in range(0,genome_size-kmer_size+1):
    current_kmer = text[i:i+kmer_size]
    if current_kmer not in kmer_array: kmer_array.append(current_kmer)

for kmer in kmer_array:
    mutated_kmer_array.append(kmer)
    for mutant in list(mismatch(kmer,"ATGC",d)):
        if mutant not in mutated_kmer_array: mutated_kmer_array.append(mutant)

#print mutated_kmer_array

for kmer in mutated_kmer_array:
    for j in range(genome_size-kmer_size+1):
        match_to = text[j:j+kmer_size]
        mismatches = 0
        for k in range(kmer_size):
            if kmer[k] != match_to[k]: mismatches = mismatches + 1
        if mismatches <= d:
            print kmer, match_to, d
            if kmer in kmer_dict.keys(): kmer_dict[kmer] = kmer_dict[kmer] + 1
            else: kmer_dict[kmer] = 1




print kmer_dict
print max(kmer_dict.values())
for (k,v) in kmer_dict.items():
    if kmer_dict[k] == max(kmer_dict.values()):
        print k,