import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
names = input().split()
id = {
    names[i]: i
    for i in range(n)
}


adj = [[] for i in range(n + m)]

for org in range(m):
    k = int(input())
    for name in input().split():
        adj[id[name]].append(n + org)
        adj[n + org].append(id[name])

# BFS
d = [-1 for i in range(n + m)]

source = id['Alice']
queue = [source]
d[source] = 0
for u in queue:
    for v in adj[u]:
        if d[v] == -1:
            d[v] = d[u] + 1
            queue.append(v)

print(*[-1 if x == -1 else x//2 for x in d[:n]])
