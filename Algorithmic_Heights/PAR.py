__author__ = 'ravi'

def partition(array,num):
    for i in range(0,len(array)):
        current_num = array[i]
        if current_num <= num:
            del array[i]
            array.insert(0,current_num)
    return array



fh = open('rosalind_par.txt','rU')

n = int(fh.readline().strip())
A = map(int,fh.readline().strip().split())

fh.close()

print ' '.join(map(str,partition(A,A[0])))