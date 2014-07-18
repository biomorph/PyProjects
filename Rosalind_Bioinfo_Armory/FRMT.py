__author__ = 'ravi'
from Bio import Entrez
from Bio import SeqIO

def len_SeqRecord (record):
    return len(record.seq)

in_file = open("rosalind_frmt.txt",'rU')

ids = in_file.readline().split()

Entrez.email = ""

handle = Entrez.efetch(db="nucleotide",id=ids, rettype="fasta")

records = list(SeqIO.parse(handle,"fasta"))

shortest_record = sorted(records,key=len_SeqRecord)[0]

print ">" + shortest_record.description
print shortest_record.seq




