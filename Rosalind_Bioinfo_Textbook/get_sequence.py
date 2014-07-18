__author__ = 'ravi'
import sys
import commands
import os
import subprocess

in_file = sys.argv[1]

input_filename = os.path.abspath(os.path.join("/Users/ravi/Desktop/DNA_ME/bismark_cov", in_file))
cov_fh = open(input_filename, 'rU')
output_filename = os.path.abspath(os.path.join("/Users/ravi/Desktop/DNA_ME/methylKitIN", in_file + "methylKitIN"))
output_fh = open(output_filename, 'w+')
for line in cov_fh:
    orig_line = line.strip()
    entries = line.split()
    chr = entries[0]
    meth_C = int(entries[4])
    unmeth_C = int(entries[5])
    start = int(entries[1])
    search_string = chr + ":" + str(start) + "-" + str(start)
    command = "samtools faidx /Users/ravi/Desktop/DNA_ME/hg19.fa" + " " + search_string + " | " + "tail -1"
    output1 = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]
    #output = commands.getoutput(command)
    #print output1
    if output1 == "C" or output1 == "c":
        bed_line = orig_line + "\t" + str(meth_C + unmeth_C) + "\t" + "+" + "\n"
        output_fh.write(bed_line)
    else:
        bed_line = orig_line + "\t" + str(meth_C + unmeth_C) + "\t"  "-" + "\n"
        output_fh.write(bed_line)

cov_fh.close()
output_fh.close()


