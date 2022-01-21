m = int(input())

raw_rects = []
if m % 3 == 0:
    n = 6
    raw_rects = [
        (0, 0, 2, 3),
        (0, 3, 2, 3),
        (2, 0, 4, 6)
    ]

elif m % 3 == 1:
    n = 12
    raw_rects = [
        (0, 0, 6, 4),
        (0, 4, 6, 4),
        (0, 8, 6, 4),
        (6, 0, 6, 9),
        (6, 9, 2, 3),
        (8, 9, 2, 3),
        (10, 9, 2, 3)
    ]

elif m % 3 == 2:
    n = 18
    raw_rects = [
        (0, 0, 12, 8),
        (0, 8, 12, 8),
        (0, 16, 3, 2),
        (3, 16, 3, 2),
        (6, 16, 3, 2),
        (9, 16, 3, 2),
        (12, 0, 6, 9),
        (12, 9, 6, 9)
    ]

# Find the largest t such that 2^t divides both h and w,
#  then returns 4^t
def get_cap(re):
    r, c, h, w = re
    for t in range(30):
        if (h & (1 << t)) | (w & (1 << t)):
            return 1 << (t << 1)
    
    assert(False)

cap = sum(get_cap(re) for re in raw_rects)

shft = 0
while cap*(1 << (shft << 1)) < m:
    shft += 1
n <<= shft

rects = list(
    tuple(val << shft for val in re)
    for re in raw_rects
)
painting = []

total = len(rects)
while total < m:
    re = rects.pop()
    r, c, h, w = re
    
    if (h & 1) | (w & 1):  # This rect can't be subdivided any more
        painting.append(re)
    else:
        total -= 1
        for i in range(2):
            for j in range(2):
                total += 1
                rects.append((
                    r + i*(h >> 1),
                    c + j*(w >> 1),
                    h >> 1,
                    w >> 1
                ))

painting.extend(list(rects))

painting.sort()
grid = [
    ['#' for j in range(n)]
    for i in range(n)
]
for r, c, h, w in painting:
    done = set()
    if r > 0:
        for j in range(w):
            done.add(grid[r - 1][c + j])
    if r + h < n:
        for j in range(w):
            done.add(grid[r + h][c + j])
    if c > 0:
        for i in range(h):
            done.add(grid[r + i][c - 1])
    if c + w < n:
        for i in range(h):
            done.add(grid[r + i][c + w])

    color = '#'
    for x in range(26):
        col = chr(ord('A') + x)
        if col not in done:
            color = col
            break
    assert(color != '#')

    for i in range(h):
        for j in range(w):
            grid[r + i][c + j] = color

print(n)
for row in grid:
    print(''.join(row))
