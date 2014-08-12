__author__ = 'ravi'
n = 5
m = 6
#A = [(1,10),(2,20),(3,30), (4,40), (5,50)]
A = [10, 20, 30, 40, 50]
k = [40, 10, 35, 15, 40, 20]

fh = open('rosalind_bins.txt','rU')
data = fh.readlines()
n,m,A,k = int(data[0]),int(data[1]),map(int,data[2].split()),map(int,data[3].split())


def bin_search(ki, A_sub):
    half = int(len(A_sub)/2)
    if half > 0:
        if ki < A_sub[half][1]:
            bin_search(ki, A_sub[:-half])
        elif ki > A_sub[half][1]:
            bin_search(ki, A_sub[-half:])
        else:
            print A_sub[half][0],
    else:
        if ki == A_sub[0][1]: print A_sub[0][0],
        print -1,


for i, a in enumerate(A):
    A[i] = (i+1, a)


for num in k:
    bin_search(num, A)
