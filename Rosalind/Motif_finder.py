__author__ = 'ravi'

sub_fh = open("rosalind_subs.txt",'rU')
(s,t) = sub_fh.read().split()
i = 0
match_list = ""
while i < len(s):
    sub_str = s[i:i+len(t)]
    if sub_str == t: match_list = match_list + " " + str(i+1)
    i = i + 1
print match_list