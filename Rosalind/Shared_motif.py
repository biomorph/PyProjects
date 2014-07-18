__author__ = 'ravi'
import re

# return a list of fasta sequences
def get_fasta_list(fasta_fh):
    fasta_dict = {}
    fasta_id = ""
    for line in fasta_fh:
        if (re.search(r'^>', line)):
            fasta_id = line.strip().replace(">","")
            fasta_dict[fasta_id] = ""
        else:
            fasta_dict[fasta_id] = fasta_dict[fasta_id] + line.strip()

    return fasta_dict.values()

#check if given search_term is present in all the sequences in the list (except the shortest sequence)
def is_in_all_sequences (search_term, sequence_list):
    #print sequence_list
    i = 0
    for sequence in sequence_list:
        if sequence.find(search_term) != -1: i = i + 1
    if i == len(sequence_list):return True
    else: return False

fasta_fh = open("rosalind_lcsm.txt", 'rU')


sequences = get_fasta_list(fasta_fh)

sequences.sort(key=lambda x:len(x)) # sort sequences by length so I can use the shortest sequence to query the rest

i = 0 # position index for the shortest sequence
window = 2 # starting with sliding window size 2 and increasing it if match is found in other sequences
shortest_sequence = sequences[0]
search_term = ""
shared_motifs = [] # list of all possible shared motifs, I will pick the longest one at the end

while i < len(shortest_sequence) and window < len(shortest_sequence)-1: #run this loop to slide window till the end of the shortest string
    search_term = shortest_sequence[i:i+window] # search for the motif within a window of size "window" at index "i"
    if is_in_all_sequences(search_term,sequences[1:]):
        window = window + 1 # increase window size if match found in all sequences
        shared_motifs.append(search_term) # append this search_term to shared_motifs list
    else:
        i = i + 1 # if no match of current window found in other sequences, slide the window to next index



shared_motifs.sort(key=lambda x:len(x), reverse=True) #sort shared_motifs based on size
print shared_motifs[0] #print the longest shared motif