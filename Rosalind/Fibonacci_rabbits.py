__author__ = 'ravi'
import time
fib_dic = {}
def total_rabbits_dynamic (n,k):
    no_of_pairs = 1
    if n >2: no_of_pairs = total_rabbits_dynamic(n-1,k) + k * total_rabbits_dynamic(n-2,k)
    return no_of_pairs

def total_rabbits_recursion (n,k):
    a,b = 1,0
    for i in range(n):
        a, b = a+k*b, a
    return b


def total_rabbits_dict (n, k):
    args = (n,k)
    if args in fib_dic: return fib_dic[args]
    no_of_pairs = 1
    if n >2:
        no_of_pairs = total_rabbits_dict(n-1,k) + k * total_rabbits_dict(n-2,k)
        fib_dic[args] = no_of_pairs
    return no_of_pairs

f = open('rosalind_fib.txt','rU')
params = f.read().strip().split(" ")
f.close()
n = int(params[0])
k = int(params[1])
start_time = time.time()

print total_rabbits_recursion(n,k)
print "recursion time %f" %(time.time()-start_time)

start_time = time.time()

print total_rabbits_dynamic(n,k)
print "recursion time %f" %(time.time()-start_time)

start_time = time.time()

print total_rabbits_dict(n,k)
print "recursion time %f" %(time.time()-start_time)

