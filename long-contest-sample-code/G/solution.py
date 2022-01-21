INF = 10**9

n = int(input())
s = input()

flags = ['A', 'C']
ans = {
    flag: [INF for i in range(n)]
    for flag in flags
}

for i in range(n):
    if s[i] in flags:
        ans[s[i]][i] = 0

        for j in range(i+1, n):
            if s[j] == '.':
                ans[s[i]][j] = min(ans[s[i]][j], j - i)
            else:
                break

        for j in range(i-1, -1, -1):
            if s[j] == '.':
                ans[s[i]][j] = min(ans[s[i]][j], i - j)
            else:
                break

for flag in flags:
    print(*[x if x < INF else -1 for x in ans[flag]])
