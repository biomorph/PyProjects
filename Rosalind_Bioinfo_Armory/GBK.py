__author__ = 'ravi'
from Bio import Entrez

in_file = open("rosalind_gbk.txt",'rU')

search_info = in_file.readlines()
genus = search_info[0].strip()
start_date = search_info[1].strip()
end_date = search_info[2].strip()

Entrez.email = "ravi.alla@berkeley.edu"

search_term = '"' + genus + '"' + "[Organism] AND" + '("' + start_date + '"[PDAT] :' +  '"' + end_date + '"[PDAT])'

handle = Entrez.esearch(db="nucleotide",term=search_term)

record = Entrez.read(handle)

print record["Count"]