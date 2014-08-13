__author__ = 'ravi'
fh = open('rosalind_ms.txt','rU')

n = int(fh.readline().strip())
A = map(int,fh.readline().strip().split())

fh.close()


B = []

for i in range(0,n,2):
    B.append(sorted(A[i:i+2]))


def merge(a,b):
    merged_array = []
    i = 0
    j = 0
    while i < len(a) and j< len(b):
        if a[i] > b[j]:
            merged_array.append(b[j])
            j += 1
        else:
            merged_array.append(a[i])
            i += 1
    if i < len(a): merged_array.extend(a[i:])
    elif j < len(b): merged_array.extend(b[j:])
    return merged_array

while len(B) > 1:
    sub_array1 = B.pop()
    sub_array2 = B.pop()
    merged_array = merge(sub_array1,sub_array2)
    B.insert(0,merged_array)

print ' '.join(map(str,B[0]))