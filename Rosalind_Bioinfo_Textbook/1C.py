__author__ = 'ravi'
import re

input_fh = open("rosalind_1c.txt",'rU')

pattern = input_fh.readline().strip()

genome = input_fh.readline().strip()


regex = re.compile('(?=%s)'%pattern)

matches = re.finditer(regex, genome)

for match in matches:
    print match.start(0),