__author__ = 'ravi'
import Translate_rna
import Overlap_graph
import re

fasta = open("rosalind_splc.txt",'rU')
fasta_dict = Overlap_graph.get_fasta_dict(fasta)
fasta.close()

sequences = sorted(fasta_dict.values(),key=len, reverse=True)

pre_mRNA = sequences[0]
introns = sequences[1:]
mature_RNA = ""
#print pre_mRNA
for intron in introns:
    intron_pattern = re.compile(intron)
    for match in re.finditer(intron_pattern,pre_mRNA):
        #print match.start(), match.end()
        mature_RNA = pre_mRNA[:match.start()] + pre_mRNA[match.end():]
        pre_mRNA = mature_RNA

codon_fh = open("codon_table_DNA.txt",'rU')
Translate_rna.translate(codon_fh,mature_RNA)
codon_fh.close()
