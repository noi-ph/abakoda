n, h, k = map(int, input().split())
points = [
    map(int, input().split())
    for i in range(n)
]

'''
We can move the sqrt out of the max because
 squaring is an increasing function.
By taking the sqrt only at the end, we only
 have to perform one floating point operation.
'''
farthest = max((x - h)**2 + (y - k)**2 for x, y in points)**0.5

print(f"{2 * farthest:.12f}")
