__author__ = 'ravi'
from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
import os

my_seq = Seq("ATTGGAATTCCTT",IUPAC.unambiguous_dna)
print repr(my_seq)
print my_seq.reverse_complement()

"""
Entrez.email = "ravi.alla@berkeley.edu"
#handle1 = Entrez.einfo(db="nucleotide")
#record1 = Entrez.read(handle1)
#print record1
handle = Entrez.esearch(db="nuccore",term="Cypripedioideae[Orgn]",rettype="fasta")
record = Entrez.read(handle)

fasta_fh=open("Cypripedioideae.gbk",'a')
for records in record["IdList"]:
    handle = Entrez.efetch(db="nucleotide", id = records, rettype="gb", retmode="text")
    fasta_fh.write(handle.read())

fasta_fh.close()
"""

for seq_record in SeqIO.parse("Cypripedioideae","fasta"):
    seq_record.annotations["Organism"] = "Cypripedioideae"
    print seq_record.annotations

"""
for seq_record in SeqIO.parse("Cypripedioideae","fasta"):
    print seq_record.id
    print repr(seq_record.seq)
    print GC(seq_record.seq)
    print seq_record.annotations["Organism"]
"""