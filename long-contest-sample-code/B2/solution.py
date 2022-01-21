n = int(input())
x = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))

if not (x[0] <= c[0]):
    print(0)
else:
    only = [0 for i in range(n)]
    ptr = 0
    for i in range(n):
        while ptr+1 < n and x[ptr+1] <= c[i]:
            ptr += 1
        only[ptr] += 1

    ans = 1
    valid = 0
    for i in range(n-1, -1, -1):
        valid += only[i]
        ans *= valid
        valid -= 1

    print(ans)
