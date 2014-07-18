__author__ = 'ravi'
import re
import sys


def make_dna_matrix(fasta_fh):
    seq_matrix = []
    i = -1;
    for line in fasta_fh:
        if not re.search(r'^>', line):
            seq_matrix[i] = seq_matrix[i] + line.strip()
        else:
            seq_matrix.append("")
            i = i + 1
    return seq_matrix


def get_profile_matrix (seq_matrix):
    A = ["A:"]
    C = ["C:"]
    G = ["G:"]
    T = ["T:"]
    j = 0
    while j < len(seq_matrix[0]):
        i = 0
        num_A = 0
        num_C = 0
        num_G = 0
        num_T = 0
        while i < len(seq_matrix):
            if seq_matrix[i][j] == "A": num_A = num_A + 1
            if seq_matrix[i][j] == "C": num_C = num_C + 1
            if seq_matrix[i][j] == "G": num_G = num_G + 1
            if seq_matrix[i][j] == "T": num_T = num_T + 1
            i = i + 1
        A.append(num_A)
        C.append(num_C)
        G.append(num_G)
        T.append(num_T)
        j = j + 1
    return (A,C,G,T)

def print_profile_matrix (profile_matrix_tuple):
    for base in (profile_matrix):
        k = 0
        while k < len(profile_matrix[0]):
            print base[k],
            k = k + 1
        print ""
    return

fasta = open("rosalind_cons.txt",'rU')

profile_matrix = get_profile_matrix (make_dna_matrix(fasta))

i = 1
while i < len(profile_matrix[0]):
    temp_list = [(profile_matrix[0][i],"A"),(profile_matrix[1][i],"C"),(profile_matrix[2][i],"G"),(profile_matrix[3][i],"T")]
    temp_list.sort(reverse= True)
    sys.stdout.write(temp_list[0][1])
    i = i + 1

print ""
print_profile_matrix(profile_matrix)
