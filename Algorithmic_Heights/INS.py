__author__ = 'ravi'
fh = open('rosalind_ins.txt','rU')

n = int(fh.readline().strip())

A = fh.readline().strip().split()
A = map(int,A)
#A = [6, 10, 4, 5, 1, 2]
#n = 6
num_swaps = 0
for i in range(1,n):
    k = i
    while k > 0 and A[k] < A [k-1]:
        A[k], A[k-1] = A[k-1], A[k]
        num_swaps += 1
        k -= 1

print A
print num_swaps