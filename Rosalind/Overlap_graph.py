__author__ = 'ravi'
import re

def get_fasta_dict(fasta_fh):
    fasta_dict = {}
    fasta_id = ""
    for line in fasta_fh:
        if (re.search(r'^>', line)):
            fasta_id = line.strip().replace(">","")
            fasta_dict[fasta_id] = ""
        else:
            fasta_dict[fasta_id] = fasta_dict[fasta_id] + line.strip()

    return fasta_dict


if __name__=='__main__':

    fasta_dict = get_fasta_dict(open("rosalind_graph.txt",'rU'))

    for fasta in fasta_dict:
        for matching_fasta in fasta_dict.keys():
            if fasta != matching_fasta and fasta_dict[fasta] != fasta_dict[matching_fasta] and fasta_dict[fasta][-3:] == fasta_dict[matching_fasta][0:3]:
                print fasta + " " + matching_fasta
