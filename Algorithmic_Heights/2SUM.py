__author__ = 'ravi'
fh = open('rosalind_2sum.txt','rU')
k, n = map(int,fh.readline().strip().split())
for line in fh:
    p,q = 0,0
    array = map(int,line.strip().split())
    for i, number in enumerate(array):
        for j in range(i+1,n):
            if number + array[j] == 0:p,q = i+1,j+1

    if p>0 or q>0: print p,q
    else: print -1