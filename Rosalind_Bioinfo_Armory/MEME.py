__author__ = 'ravi'
import os
import re

cmd = '~/bin/meme.bin rosalind_meme.txt -o meme_out -protein'

os.system (cmd)

meme_out_fh = open("meme_out/meme.txt", 'rU')

for line in meme_out_fh:
    if re.search(r'regular expression', line):
       next(meme_out_fh)
       print next(meme_out_fh)







