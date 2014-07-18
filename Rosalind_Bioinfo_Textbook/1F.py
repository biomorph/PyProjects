__author__ = 'ravi'

input_fh = open("rosalind_1f.txt",'rU')

pattern = input_fh.readline().strip()

text = input_fh.readline().strip()

d = int(input_fh.readline().strip())

k_mer_size = len(pattern)

genome_size = len(text)

sub_strings = []

for i in range(0, genome_size - k_mer_size + 1):
    sub_strings.append((text[i:i+k_mer_size],i))

print sub_strings
for sub_string in sub_strings:
    mismatch_count = 0
    for j in range(0,k_mer_size):
        if sub_string[0][j] != pattern[j]: mismatch_count += 1
    if mismatch_count <= d:
        print sub_string[1]

