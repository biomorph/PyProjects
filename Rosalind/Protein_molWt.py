__author__ = 'ravi'

mw_fh = open("aa_MW.txt",'rU')
mw_dict = {}
for line in mw_fh:
    aa = line.strip().split("   ")[0]
    wt = line.strip().split("   ")[1]
    mw_dict[aa] = float(wt)
mw_fh.close()

prot_fh = open("rosalind_prtm.txt",'rU')

protein = prot_fh.read().strip()
mw = 0
for aa in protein:
    mw = mw + mw_dict[aa]
print mw
