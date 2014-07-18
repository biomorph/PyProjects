__author__ = 'ravi'
import urllib2
import re


def get_fasta_from_url (url):
    fasta_url = urllib2.urlopen(url)
    fasta = []
    sequence = ""
    for line in fasta_url:
        if re.search(r'^>',line): fasta.append(line.strip())
        else: sequence = sequence + line.strip()
    fasta.append(sequence)
    return fasta

def get_accessions_list (acc_file):
    acc_list = []
    for line in acc_file: acc_list.append(line.strip())
    return acc_list


acc_file = open("rosalind_mprt.txt",'rU')

for accession in get_accessions_list(acc_file):
    acc_url = "http://www.uniprot.org/uniprot/" + accession + ".fasta"
    sequence = get_fasta_from_url(acc_url)[1]
    #print accession
    #print sequence
    if re.search (r'N[^P][ST][^P]',sequence):
        motif_matches = re.finditer(r'(?=N[^P][ST][^P])',sequence)
        print ""
        print accession
        for match in motif_matches:
            location = match.start() + 1
            print location,



