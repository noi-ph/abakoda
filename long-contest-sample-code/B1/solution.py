n = int(input())
print(
    "YES"
    if all(
        x <= y
        for x, y in zip(
            sorted(map(int, input().split())),
            sorted(map(int, input().split()))
        )
    )
    else "NO"
)
