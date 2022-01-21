conv = {
    'U': (0, 1),
    'D': (0, -1),
    'RU': (1, 0),
    'LD': (-1, 0),
    'RD': (1, -1),
    'LU': (-1, 1)
}

n = int(input())
loc = {}
for i in range(n):
    username = input()
    m = int(input())

    x, y = 0, 0
    for _ in range(m):
        t, k = input().split()
        k = int(k)
        dx, dy = conv[t]
        x += k*dx
        y += k*dy

    loc[username] = (x, y)

for _ in range(int(input())):
    u, v = input().split()

    x1, y1 = loc[u]
    x2, y2 = loc[v]
    x, y = x1-x2, y1-y2

    if (x > 0) == (y > 0):
        print(abs(x) + abs(y))
    else:
        print(max(abs(x), abs(y)))
