__author__ = 'ravi'
def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

fh = open('rosalind_hea.txt','rU')

n = int(fh.readline().strip())

A = map(int,fh.readline().strip().split())

build_max_heap(A)

def is_heap(A):
    return all(A[i] <= A[(i - 1) // 2] for i in range(1, len(A)))


print is_heap(A)