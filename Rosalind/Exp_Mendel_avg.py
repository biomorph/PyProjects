__author__ = 'ravi'
gentype_pair_nums = open("rosalind_iev.txt", 'rU').read().split()
expected_dominant = 2*float(gentype_pair_nums[0]) + 2*float(gentype_pair_nums[1]) + 2*float(gentype_pair_nums[2]) + 1.5*float(gentype_pair_nums[3]) + 1*float(gentype_pair_nums[4]) + 0*float(gentype_pair_nums[5])

print expected_dominant