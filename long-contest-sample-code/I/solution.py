import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
names = input().split()
id = {
    names[i]: i
    for i in range(n)
}

my_orgs = [[] for i in range(n)]
my_members = [[] for i in range(m)]

for org in range(m):
    k = int(input())
    for name in input().split():
        my_orgs[id[name]].append(org)
        my_members[org].append(id[name])

alice_number = [-1 for i in range(n)]
done = [False for org in range(m)]

source = id['Alice']
queue = [source]
alice_number[source] = 0
for person in queue:
    for org in my_orgs[person]:
        if not done[org]:
            done[org] = True
            for orgmate in my_members[org]:
                if alice_number[orgmate] == -1:
                    alice_number[orgmate] = alice_number[person] + 1
                    queue.append(orgmate)

print(*alice_number)
