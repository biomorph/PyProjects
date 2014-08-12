__author__ = 'ravi'
fh = open('rosalind_cc.txt', 'rU')

node_dict = {}
n, m = map(int, fh.readline().strip().split())
for line in fh:
    line = line.strip().split()
    node1 = int(line[0])
    node2 = int(line[1])
    if node1 in node_dict:
        node_dict[node1].add(node2)
    else:
        node_dict[node1] = set([node2])
    if node2 in node_dict:
        node_dict[node2].add(node1)
    else:
        node_dict[node2] = set([node1])

print node_dict


def dfs(graph, start, visited=None):
    if visited == None: visited = set()
    if start not in graph:
        visited.add(start)
        return visited
    if start not in visited: visited.add(start)
    for next in sorted([x for x in graph[start] if x not in visited]):
        dfs(graph,next,visited)
    return visited


visited_set = frozenset(dfs(node_dict,1))
unique_sets = set()
unique_sets.add(visited_set)

number_cc = 0
for node in range(2,n+1):
    visited_set = frozenset(dfs(node_dict,node))
    unique_sets.add(visited_set)
print len(unique_sets)