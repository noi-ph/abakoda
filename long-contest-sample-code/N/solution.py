from string import ascii_uppercase

r, c = map(int, input().split())
grid = [
    input()
    for i in range(r)
]

exists = {
    ch: False
    for ch in ascii_uppercase
}
for row in grid:
    for ch in row:
        exists[ch] = True

n = int(input())
ops = [
    input().split()
    for i in range(n)
]

relevant_ops = []
invertible = True
for x, iss, y in ops:
    if x != y:
        if exists[x]:
            if exists[y]:
                invertible = False
                break
            else:
                relevant_ops.append((x, iss, y))
                exists[x] = False
                exists[y] = True

if invertible:
    print("YES")
    print(len(relevant_ops))
    for x, iss, y in reversed(relevant_ops):
        print(y, iss, x)

else:
    print("NO")
