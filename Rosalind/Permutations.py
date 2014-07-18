__author__ = 'ravi'

import random
n = 10
#num_list = range(1,n+1,1)
s = set()
i = 0
while i < 10000000:
    random_list = " ".join(str(x) for x in random.sample(range(1,n+1,1),n))
    s.add (random_list)
    i = i + 1
print len(s)
for permutation in s:
    j = 0
    while j < len(permutation):
        print permutation[j],
        j = j + 1

    print ""
