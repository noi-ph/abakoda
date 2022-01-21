def sgn(x):
    return -1 if x < 0 else 1

# floating point equals
def feq(a, b, eps=1e-4):
    return abs(a - b) < eps

for _ in range(int(input())):
    w, h, dx, dy = map(int, input().split())

    step_count = 0
    step_size = (dx**2 + dy**2)**0.5

    # Center the box at the origin.
    # Leveraging symmetry lets us simplify
    #  the edge collision logic.
    x, y = -w/2, -h/2
    bounces = 0
    while True:
        time_to_H = abs(sgn(dy)*h/2 - y) / abs(dy)
        time_to_V = abs(sgn(dx)*w/2 - x) / abs(dx)
        t = min(time_to_H, time_to_V)
        
        x += t*dx
        y += t*dy
        step_count += t

        if feq(abs(x), w/2) and feq(abs(y), h/2):
            break
        if feq(abs(x), w/2):
            dx *= -1
        if feq(abs(y), h/2):
            dy *= -1

        bounces += 1

    print(step_count * step_size)
    print(bounces)
    print(('T' if y > 0 else 'B') + ('R' if x > 0 else 'L'))
