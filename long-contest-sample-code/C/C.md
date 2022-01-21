## Caught In Candy

<details closed>
<summary>Hint 1</summary>

If you were _given_ a fixed radius for the circle, how do you determine which nuts lie on or within that circle?

</details>

<details closed>
<summary>Solution</summary>

We see that a nut will be on or within circle if and only if the radius of the circle is greater than or equal to the distance from the center of the circle to that nut.  Thus, the smallest radius which contains all the points must be the greatest such distance from the center of the circle to any of the nuts.  Using the distance formula, the answer is thus,
$$
    2 \times \max_{1 \leq i \leq n} \sqrt{(x_i - h)^2 + (y_i - k)^2}.
$$
Note that we multiply by $2$, because the problem asks for the diameter of the final circle.

Also, note that $\sqrt{x}$ is an increasing function, so this value is the same as computing,
$$
    2 \times \sqrt{\max_{1 \leq i \leq n}\left((x_i - h)^2 + (y_i - k)^2\right)}.
$$
In simple terms, we only need to compare using the _squares_ of the distances, because the nut that is a maximum distance away from $(h, k)$ is also the _same_ nut that is a maximum square distance away from $(h, k)$.  The nice thing about this is that we only need to perform one square root right at the very end.  Avoiding floating point operations is always preferable if possible.

</details>

<details closed>
<summary>Bonus</summary>

What if we are free to center the circle wherever we like?  In other words, given _just_ the set of points, find the center and radius of the smallest circle that contains all of the given points.  

This version is well-known, often called the **minimum bounding circle** or **smallest encloding circle** problem.  Many solutions to it exist, at various levels of difficulty and efficiency.

- A straightforward $\mathcal{O}(n^4)$ exists that considers all possible pairs and triplets of points (can you think of it?)
- The editorial for [ABC151 F - Enclose All](https://atcoder.jp/contests/abc151/tasks/abc151_f) contains an outline for a roughly $\mathcal{O}(n^3 \lg \varepsilon^{-1})$ solution, where $\varepsilon$ is the desired precision of the final answer.
- [This Quora post](https://www.quora.com/What-is-an-algorithm-for-enclosing-the-maximum-number-of-points-in-a-2-D-plane-with-a-fixed-radius-circle) details a slightly-more-involved $\mathcal{O}(n^2 \lg n)$ solution.
- There also exists an $\mathcal{O}(n \log n)$ algorithm, as well as an $\mathcal{O}(n)$ randomized algorithm, both of which you can read up on in the [Wikipedia article](https://en.wikipedia.org/wiki/Smallest-circle_problem) for this problem.

</details>