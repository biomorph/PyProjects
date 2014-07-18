__author__ = 'ravi'
import re


def construct_kmer_list (string, kmer_size):
    i = 0
    kmer_list = []
    while i < len(string)-kmer_size+1:
        current_kmer = string[i:i+kmer_size]
        if current_kmer not in kmer_list: kmer_list.append(current_kmer)
        i = i + 1
    return kmer_list


def count(Text, pattern):
    regex = re.compile('(?=%s)'%pattern)
    matches = re.findall(regex,Text)
    return len(matches)
def fn(s):
    return dict[s]

def main():

    input_fh = open("rosalind_1a.txt",'rU')

    Text = input_fh.readline().strip()

    k_size = int(input_fh.readline().strip())


    kmer_list = construct_kmer_list(Text,k_size)

    dict = {}

    for kmer in kmer_list:
        dict [kmer] = count(Text,kmer)
    max_count = max(dict.values())

    for pattern, pattern_count in dict.items():
        if pattern_count == max_count: print pattern,
if __name__ == "__main__":
    main()