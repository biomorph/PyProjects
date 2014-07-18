__author__ = 'ravi'
dna_fh = open("rosalind_hamm.txt",'ru')

s_t = dna_fh.readlines()
dna_fh.close()
print s_t
ham_dist = 0

for i in range(len(s_t[0])):
    if s_t[0][i] != s_t[1][i]:ham_dist =  ham_dist + 1

print ham_dist
