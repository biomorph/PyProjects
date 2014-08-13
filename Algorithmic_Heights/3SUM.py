__author__ = 'ravi'
fh = open('rosalind_3sum.txt','rU')
k, n = map(int,fh.readline().strip().split())


def sum_ind(sum, dict, i, j):
    if -1*sum in dict and sum!= 0:  # if sum is not zero and -ve of sum is in the dict, return indices of the sum and key value of -ve sum in the dict
        return sorted([i+1, j+1, dict[-1*sum]+1])

    elif sum == 0 and sum in dict and dict[sum] != i and dict[sum] != j:   # if sum is zero, make sure that its index in the array is not the same as the key value of zero in the dict
        return sorted([i+1, j+1, dict[0]+1])


for line in fh:
    array = map(int,line.strip().split())
    dict = {}

    for index, number in enumerate(array):
        dict[number] = index
    indices = []
    for i, num in enumerate(array):
        for j in range(i+1,n):
            sum = array[i] + array[j]
            indices = sum_ind(sum,dict, i, j)
            if indices: break
        if indices: break


    if indices:
        print ' '.join(map(str,indices))
    else: print '-1'

fh.close()