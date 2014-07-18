import itertools

d = 2
text = "AGTGATCC"
#for i in range(1,d+1):
 #   for combo in itertools.combinations(range(0,len(text)),i):
        #for index in combo:
        #print " ".join(map(str,combo))


def mismatch(word, letters, num_mismatches):
    for locs in itertools.combinations(range(len(word)), num_mismatches):
        this_word = [char for char in word]
        print this_word
        for loc in locs:
            orig_char = word[loc]
            this_word[loc] = [l for l in letters if l != orig_char]
        print this_word
        for poss in itertools.product(*this_word):
            yield ''.join(poss)

print list(mismatch(text,"ATGC",d))