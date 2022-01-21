import sys
def input():
    return sys.stdin.readline().rstrip()

r, c = map(int, input().split())
grid = [input() for _ in range(r)]

ans = {}
for _ in range(int(input())):
    t, s = input().split()
    s = int(s)

    if t == 'R':
        i, j = s, c
        di, dj = 0, -1

    elif t == 'T':
        i, j = 1, s
        di, dj = 1, 0

    elif t == 'L':
        i, j = s, 1
        di, dj = 0, 1

    elif t == 'B':
        i, j = r, s
        di, dj = -1, 0
    
    else:
        assert(False)

    while 1 <= i <= r and 1 <= j <= c:
        if grid[i - 1][j - 1] == '/':
            di, dj = -dj, -di
        else:
            di, dj = dj, di

        i += di
        j += dj

    if i == 0:
        label, num = 'T', j

    elif i == r + 1:
        label, num = 'B', j

    elif j == 0:
        label, num = 'L', i
        
    elif j == c + 1:
        label, num = 'R', i

    print(label, num)
