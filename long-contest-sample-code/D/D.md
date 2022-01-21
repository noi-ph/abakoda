## Decorum Sensing

<details closed>
<summary>Hint 1</summary>

Take a look at the values of $A_i$ of the students that do say "Thank you, sir!", and the order in which these values are said.  Do you notice something?

</details>

<details closed>
<summary>Solution</summary>

We need one key insight. For a student to decide whether or not they will say "Thank you, sir!", it is sufficient for them to _only_ observe the other students with a strictly smaller $A$ value.

We can develop the following algorithm.
- Maintain some variable `done` which counts the number of students that have already said "Thank you, sir!" (initialized to $0$).
- Sort $A$ in nondecreasing order.
- Iterate over the students' $A$ values in that sorted order.
  - If some student's $A$ value is less than or equal to `done`, then this student also says, "Thank you, sir!" (so increment `done += 1`)
  - If not, then we can actually `break` and exit the loop early, because no further students from this point on will say, "Thank you, sir!"

The running time of this solution is $\mathcal{O}(n \lg n)$, to sort $A$.

</details>

