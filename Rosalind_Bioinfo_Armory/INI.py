__author__ = 'ravi'
from Bio.Seq import Seq

in_file = open("rosalind_ini.txt",'rU')

for line in in_file:
    sequence = Seq(line.strip())
    print ("%d %d %d %d" %((sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T"))))

in_file.close()

