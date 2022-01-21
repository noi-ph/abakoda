INF = 10**9

n = int(input())
s = input()

def go_one_direction(n, s, c, order):
    curr = INF
    nearest = [None for i in range(n)]
    for i in order:
        if s[i] == c:
            curr = 0
        elif s[i] == '.':
            curr += 1
        else:
            curr = INF

        nearest[i] = curr

    return nearest

def get_answer_array(n, s, c):
    return [
        x if x < INF else -1
        for x in (
            min(forward, backward)
            for forward, backward in zip(
                go_one_direction(n, s, c, range(n)),
                go_one_direction(n, s, c, range(n-1, -1, -1))
            )
        )
    ]

for c in ['A', 'C']:
    print(*get_answer_array(n, s, c))
