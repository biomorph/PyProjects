__author__ = 'ravi'
fh = open('rosalind_bfs.txt','rU')

node_dict = {}
n, m = map(int,fh.readline().strip().split())
for line in fh:
    line = line.strip().split()
    node1 = int(line[0])
    node2 = int(line[1])
    if node1 in node_dict: node_dict[node1].append(node2)
    else: node_dict[node1] = [node2]

distance_from_1 = {}

for i in range(2,n+1):
    distance_from_1[i]=-1

for i in range(1,n+1):
    Q = [1]
    if i == 1:
        distance_from_1[1] = 0
        pass
    while len(Q) > 0:
        u = Q[0]
        del Q[0]
        if u not in node_dict: node_dict[u] = [0]
        for v in node_dict[u]:
            if v == 0: break
            if distance_from_1[v] == -1:
                Q.append(v)
                distance_from_1[v] = distance_from_1[u] + 1


for nodes in sorted(distance_from_1.keys()):
    print distance_from_1[nodes],

