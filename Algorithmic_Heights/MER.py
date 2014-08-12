__author__ = 'ravi'
fh = open('rosalind_mer.txt','rU')

n = int(fh.readline().strip())
A = map(int,fh.readline().strip().split())
m = int(fh.readline().strip())
B = map(int,fh.readline().strip().split())


C = []
i = 0
j = 0
while i+j < m+n-1:
    if A[i] > B[j]:
        C.append(B[j])
        j += 1
    else:
        C.append(A[i])
        i += 1
if i < n: C.append(A[i])
elif j < m: C.append(B[j])

print ' '.join(map(str,C))