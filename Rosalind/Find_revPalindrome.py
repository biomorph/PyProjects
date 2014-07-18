__author__ = 'ravi'
import Reverse_Comp

dna_fh = open("rosalind_revp.txt",'rU')

dna_string = ""
for line in dna_fh:
    if line.find(">") == -1: dna_string = dna_string + line.strip()
print dna_string
window_length = 4
palindrome_info = []
while window_length <= 12:
    index = 0
    while index < len(dna_string):
        first_half_site = dna_string[index:index+(window_length)/2]
        second_half_site = dna_string[index+(window_length)/2:index+window_length]
        if Reverse_Comp.revC(first_half_site) == second_half_site:
            palindrome_info.append([index+1, window_length])
        index = index + 1
    window_length = window_length + 2


for palindrome in palindrome_info: print palindrome[0], palindrome[1]



