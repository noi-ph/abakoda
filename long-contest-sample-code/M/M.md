## Mondrianansala

<details closed>
<summary>Hint 1</summary>

The problem claims that the task is always possible for $m \geq 6$.  Can you prove this?

As a further hint, at this stage, you can momentarily forget about having to construct the ASCII grid with side length $\leq 2500$.  Focus on pen-and-paper drawings.

</details>

<details closed>
<summary>Hint 2</summary>

If we have a $2 : 3$ rectangle, we can cut it into four equal quarters by slicing it in half along its length and width.  This produces _four_ rectangles that all have the $2 : 3$ aspect ratio.

</details>

<details closed>
<summary>Hint 3</summary>

Can you draw, by hand, solutions to $m = 6, 7, 8$?  Combine this with the previous hint in order to show that the task is always possible (with a large enough square).

</details>

<details closed>
<summary>Solution</summary>

First, we ignore the final construction (with the $n \leq 2500$) requirement and show that the task should always be possible (with a large enough square).

- If we have a $2 : 3$ rectangle, we can cut it into four equal quarters by slicing it in half along its length and width.
  - This produces _four_ rectangles that all have the $2 : 3$ aspect ratio.
  - Let's call this **quartering** a rectangle.
- Suppose I have a solution with $k$ rectangles.
  - I can choose any rectangle in the solution and quarter it.
  - This produces a solution with $k - 1 + 4$ rectangles.
- I only need to construct, by hand, solutions for $m = 6, 7, 8$, to serve as our base cases.  
- For any larger $m$, I first choose the appropriate base case, depending on the remainder when $m$ is divided by $3$.
  - Then, I keep applying the "choose a rectangle and quarter it" operation as many times as needed (adding $+3$ to the rectangle count each time), until the total number of rectangles reaches the desired $m$.

This completes the proof.  Now, let's move on to implementation.  How do we go about constructing the ASCII grid?

- Let's agree to only quarter a rectangle if both its side lengths are even (that way, we only ever have rectangles with integer side lengths).
- Define the "capacity" of a rectangle to be $4^t$, where $t$ is the largest positive integer such that $2^t$ divides both the length and width of the rectangle.
  - Basically, this gives us the maximum number of rectangles that we can get by repeatedly quartering this rectangle and the resulting subrectangles.
  - For example:
    - The capacity of an $8 \times 12$ rectangle is $16$, because we can quarter it into four $4 \times 6$ rectangles, then quarter each of _those_ into four $2 \times 3$ rectangles. 
    - The capacity of a $6 \times 9$ rectangle is $1$, because it cannot be quartered.  
- The capacity of the entire painting is the sum of the capacities of each rectangle.

Now, we just need to make sure that the capacity of our base solution is $\geq m$.

- Suppose we have a base $n \times n$ solution whose capacity is $\text{cap}$.
- We can double the side lengths of every rectangle to produce a $2n \times 2n$ solution, and you can confirm that this has a capacity of $4\, \text{cap}$.
- Find the smallest integer $t$ such that $4^t  \text{cap} \geq m$, then blow up our base solution into a $2^t n \times 2^t  n$ painting.

Now, we are sure that we should be able to reach a rectangle count of $m$ just by quartering the rectangles in our base solution.  To ensure that $2^t n \leq 2500$ in all cases, we can just test it on $m = 200000, 199999, 199998$ and see if the resulting paintings are small enough.  If not, just try a different base solution.

As an implementation note, I represented my rectangles as a four-tuple $(r, c, h, w)$, where $r$ and $c$ indicate the row and column of the top-left corner, then $h$ and $w$ indicate the height and width of the rectangle.  This representation makes them easy to quarter.

The final implementation detail is figuring out how to color each rectangle such that no two touching adjacent rectangles are the same color.  You could try to come up with a cute coloring scheme, but it might also just be easier to think about just applying a greedy coloring algorithm.  For each rectangle, color it with the first letter that hasn't yet been used by any of its neighbors.  

The Four-Color Theorem tells us that the painting can always be colored using only $4$ colors.  If you wanted to get fancy and deterministic, there exists a simple linear-time algorithm for six-coloring any planar graph.  But we have _twenty-six_ colors at our disposal, so a greedy coloring is probably going to work.

The correctness of the author's solution was verified by running it against all possible inputs from $6$ to $200000$.  But you, the contestant, don't need to do that.

</details>

<details closed>
<summary>Remarks</summary>

The premise is a standard math problem used in teaching math induction.
- The most classic version asks you to decompose a square into exactly $m$ smaller squares.
- Another version asks you to decompose a square into $m$ $1 : 2$ rectangles.
  - This was asked as the A1 question in the 2018 Simon Marais Math Competition (see [here](http://www.simonmarais.org/2018.html)).
  - This was also (coincidentally) featured in a recent Numberphile video (see [here](https://www.youtube.com/watch?v=VZ25tZ9z6uI))

Solving this problem for arbitrary $p : q$ ratios is, to my knowledge, still open.  The problem seems to be that there is no general algorithm for constructing the small base cases. If you can think of such a method, it might be worthy of publication!

</details>

<details closed>
<summary>Setter's Code (Python)</summary>

```py
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

```

</details>