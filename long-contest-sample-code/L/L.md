<details closed>
<summary>Hint 1</summary>

This is just an implementation problem.  No fancy tricks are needed (other than possibly needing to use fast input).

</details>

<details open>
<summary>Solution</summary>

Note that no two paths inside the mirror maze intersect with each other.  Thus, for each "triangle" in the maze, there is at most one path that travels through it; for each "square" in the maze, there are at most _two_ paths that travel through it. And we travel through each such path at most twice (once starting from each endpoint).

# TODO

Thus, it is actually sufficient for us to just directly simulate each query.  Some paths may be longer than others, but if we start from all possible distinct starting locations, the total amount of steps traveled across all paths is only $\mathcal{O}(2\times 2 \times \text{size of the grid})$.

Here is a brief summary of the author's implementation.
- We maintain our current position, and the direction we are currently facing.
- Our current direction, along with the orientation of the mirror we are on, determine the direction of our next step.
- For each query, start at the indicated initial position and direction, then keep taking steps one at a time until we exit the grid.

The only gotcha is that for a language like Python, you probably need to use a fast method of input like `sys.stdin.readline()` instead of `input()`.
</details>