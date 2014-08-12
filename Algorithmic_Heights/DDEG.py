__author__ = 'ravi'
fh = open('rosalind_ddeg.txt','rU')

node_dict = {}
n, m = map(int,fh.readline().strip().split())
for line in fh:
    line = line.strip().split()
    node1 = int(line[0])
    node2 = int(line[1])
    if node1 in node_dict: node_dict[node1].append(node2)
    else: node_dict[node1] = [node2]
    if node2 in node_dict: node_dict[node2].append(node1)
    else: node_dict[node2] = [node1]

fh.close()

for node in range(1,n+1):
    if node in node_dict:
        neighbors = node_dict[node]
        sum_deg = sum([len(node_dict[i]) for i in neighbors])
        print sum_deg,
    else: print 0


