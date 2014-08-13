__author__ = 'ravi'
'''
for line in fh:
    p,q = 0,0
    array = map(int,line.strip().split())
    for i, number in enumerate(array):
        for j in range(i+1,n):
            if number + array[j] == 0:p,q = i+1,j+1

    if p>0 or q>0: print p,q
    else: print -1
'''

def sum2_ind(array):
    dict = {}
    for index, number in enumerate(array):
        dict[number] = index
    for i, num in enumerate(array):
        neg_number = -1*num
        if neg_number in dict and num!= 0:  # if number is not zero and  negative number is in the dict, return indices of the num and key value of negative number in the dict
            return sorted([i+1, dict[neg_number]+1])
        elif num == 0 and dict[num] != i:   # if number is zero, make sure that its index in the array is not the same as the key value of zero in the dict
            return sorted([i+1, dict[0]+1])


fh = open('rosalind_2sum.txt','rU')
k, n = map(int,fh.readline().strip().split())
for line in fh:
     array = map(int,line.strip().split())
     indices = sum2_ind(array)
     if indices:
         print ' '.join(map(str,indices))
     else: print -1