n = int(input())
A = map(int, input().split())

done = 0
for val in sorted(A):
    if val <= done:
        done += 1
    else:
        break

print(done)
