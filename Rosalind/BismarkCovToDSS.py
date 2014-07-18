__author__ = 'ravi'


cov_file = open("bismark.cov",'rU')
dss_input = open("dss.in",'w')

for line in cov_file:
    methylated_number = line.split()[4]
    total_coverage = int(line.split()[4])+int(line.split()[5])
    dss_input.write ('%s \t %s \t %s \t %d \t %s \n' %(line.split()[0], line.split()[1], line.split()[2], total_coverage, methylated_number))

