__author__ = 'ravi'



def increasing_subsequence(sequence):
    A = sequence
    n = len(A)
    B=[A[0],]
    i = 1
    while i < n:
        if A[i] > B[len(B)-1]:
            B.append(A[i])
        else:
            num_to_replace = min([x for x in B if x > A[i]])
            index_to_replace = B.index(num_to_replace)
            B[index_to_replace] = A[i]
        i = i + 1

    return B

def decreasing_subsequence(sequence):
    A = sequence
    n = len(A)
    B=[A[0],]
    i = 1
    while i < n:
        if A[i] < B[len(B)-1]:
            B.append(A[i])
        else:
            num_to_replace = max([x for x in B if x < A[i]])
            index_to_replace = B.index(num_to_replace)
            B[index_to_replace] = A[i]
        i = i + 1

    return B


sequence = [8, 2, 1, 6, 5, 7, 4, 3, 9]

print increasing_subsequence(sequence)
print decreasing_subsequence(sequence)

