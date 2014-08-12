__author__ = 'ravi'
from collections import Counter

fh = open('rosalind_maj.txt','rU')
k, n = map(int,fh.readline().strip().split())


def majority_element(a):
    # Initialize the candidate element and count.
    candidate, count = a[0], 0
    # Run through the list, updating the count and changing candidates as necessary.
    for element in a:
        count += [-1, 1][element == candidate]
        if count == 0:
            candidate, count = element, 1

    # Check if the candidate is indeed the majority element, returning the appropriate result.
    return [-1, candidate][a.count(candidate) > len(a)/2]


for line in fh:
    line = line.strip().split()
    print majority_element(line),
    #c = Counter(line)
    #if c.most_common(1)[0][1] > n/2: print int(c.most_common(1)[0][0]),
    #else: print -1,
print '\n'
fh = open('rosalind_maj.txt','rU')
k, n = map(int,fh.readline().strip().split())
for line in fh:
    line = line.strip().split()
    #print majority_element(line),
    c = Counter(line)
    if c.most_common(1)[0][1] > n/2: print int(c.most_common(1)[0][0]),
    else: print -1,