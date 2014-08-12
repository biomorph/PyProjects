__author__ = 'ravi'
fh = open('rosalind_hea.txt','rU')

n = int(fh.readline().strip())

A = map(int,fh.readline().strip().split())
A = [1] + A #adding 1 to the array to make convert from 0 based to 1 based array

'''
#Super Inefficient algorithm
def bubble_up(A,pos,can_move=False):
    i = pos-1
    while A[i] > A[(i-1)/2] and i > 0:
        A[i], A[(i-1)/2] = A[(i-1)/2], A[i]
        i = (i-1)/2
        can_move=True
    return A, can_move


can_move = True
i = n
while i > 0:
    A, can_move = bubble_up(A,i)
    if not can_move: i = i - 1
    else: i = n

print A
'''


def maxheapify(i):
    while i <= n/2:
        node = A[i]
        left_child = A[2*i] # set left child
        right_child = float("-inf")  # accounts for when the right child is missing
        if 2*i+1 < n: right_child = A[2*i+1] # only set right child when it is present
        if node < left_child and left_child >= right_child: # swap with left child and set i to next left child index
            A[i],A[2*i] = A[2*i],A[i]
            i = 2*i
        elif node < right_child and right_child >= left_child: # swap with right child and set i to next right child index
            A[i],A[2*i+1] = A[2*i+1],A[i]
            i = 2*i+1
        else: i = 2*i # increment i so the while loop stops after n/2 levels
    return A

for i in range(n/2,0,-1):
    maxheapify(i)


print ' '.join(map(str,A))

