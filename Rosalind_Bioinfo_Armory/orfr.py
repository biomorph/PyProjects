__author__ = 'ravi'
from Bio.Seq import translate
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re

dna_fh = open("rosalind_orfr.txt",'rU')

dna_sequence = Seq(dna_fh.readlines()[0].strip(),alphabet=IUPAC.unambiguous_dna)

dna_sequence_revC = dna_sequence.reverse_complement()

all_ATGs_top = re.finditer(r'ATG',str(dna_sequence))

all_ATGs_bottom = re.finditer(r'ATG',str(dna_sequence_revC))

possible_CDS = []

for ATG in all_ATGs_top:
    possible_CDS.append(str(dna_sequence)[ATG.start(0):])

for ATG in all_ATGs_bottom:
    possible_CDS.append(str(dna_sequence_revC)[ATG.start(0):])

possible_proteins = []

for CDS in possible_CDS:
    possible_proteins.append(translate(CDS,to_stop=True, stop_symbol=""))


print sorted(possible_proteins, key=len, reverse=True)[0]



