__author__ = 'ravi'
import subprocess
import re

filt_fh = open ("rosalind_filt.txt", 'rU')
fastq_fh = open("rosalind.fastq",'r+')

record = filt_fh.readlines()
params = record[0]
fastq = record[1:]

fastq_fh.writelines(fastq)

filt_fh.close()
fastq_fh.close()

q = params.split()[0]
p = params.split()[1]

cmd = "~/Downloads/bin/fastq_quality_filter -i rosalind.fastq -o rosalind_out.fastq -Q33 -v -q " + str(q) + " -p " + str(p)

output_stats = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)

matches = re.search(r'Output: (\d+)',output_stats)
print matches.group(1)
#print commands.getoutput(cmd)

