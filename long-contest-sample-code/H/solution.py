def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

for _ in range(int(input())):
    w, h, x, y = map(int, input().split())

    d = gcd(x, y)
    x //= d
    y //= d

    k = lcm(lcm(x, w) // x, lcm(y, h) // y)  # lcm(w//gcd(x,w), h//gcd(y,h))
    a, b = k*x, k*y
    hbounce = a//w - 1
    vbounce = b//h - 1

    print(f"{(a**2 + b**2)**(0.5):.12f}")
    print(hbounce + vbounce)
    print(('B' if vbounce & 1 else 'T') + ('L' if hbounce & 1 else 'R'))
