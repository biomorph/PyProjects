__author__ = 'ravi'
from Bio import ExPASy
from Bio import SwissProt
import re

in_file = open("rosalind_dbpr.txt", 'rU')

for line in in_file:
    prot_id = line.strip()
    handle = ExPASy.get_sprot_raw(prot_id)

    record = SwissProt.read(handle)

    for reference in record.cross_references:
        if (reference[0] == "GO") and (re.search(r'P:',reference[2])):
            print reference[2].split("P:")[1]


in_file.close()