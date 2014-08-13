__author__ = 'ravi'
fh = open('rosalind_mer.txt','rU')

n = int(fh.readline().strip())
A = map(int,fh.readline().strip().split())
m = int(fh.readline().strip())
B = map(int,fh.readline().strip().split())


C = []
i = 0
j = 0
while i<n and j < m:
    if A[i] > B[j]:
        C.append(B[j])
        j += 1
    else:
        C.append(A[i])
        i += 1
if i < n: C.extend(A[i:])
elif j < m: C.extend(B[j:])

print ' '.join(map(str,C))