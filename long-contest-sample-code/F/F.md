## Funny Sequence

<details closed>
<summary>Hint 1</summary>

Write a brute force program and stare at the first $20$ or so terms of the sequence.  Can you spot a pattern?

</details>

<details closed>
<summary>Solution</summary>

The sequence has a simple closed form: $a_n = n^2 + 2$.  The expected solution is to guess this pattern by examining the first few terms of the sequence.

If desired, one can then prove this fact using mathematical induction, but this is not necessary to get an Accepted verdict.

If interested, you may check `Remarks (Math)` for an outline of an alternate derivation of the closed form that relies less on seeing and guessing the magic pattern.

</details>

<details closed>
<summary>Remarks (Comp Prog)</summary>

Consider the general family of sequences defined by the recurrence relation $s_n = a \, s_{n-1} + b \, s_{n-2} + c$, where $a$, $b$, and $c$ are given constants, along with the initial values $s_0$ and $s_1$.  Computing $s_n$ can be done in $\mathcal{O}(\lg n)$ by fast matrix exponentiation.  

However, amusingly enough, $n = 3 \times 10^9$ is so large that matrix solutions to `F` will fail due to integer overflow (if the implementation only uses 64-bit data types).
</details>

<details closed>
<summary>Remarks (Math)</summary>

All sequences in this portion are indexed starting at $0$.

When doing IQ tests, a common tactic in "guess the sequence" questions is to look at the difference between consecutive terms.  
- For example, in, the sequence $2, 5, 8, 11, 14, \dots$, each pair of consecutive terms has a common difference of $3$.
- Thus, we guess that it can be described by the closed form $2 + 3n$.

In general, for some sequence $a$, we define its _difference sequence_ $d$ by the formula $d_n = a_{n+1} - a_n$.  Why is this useful?

- Note that $d_0 + d_1 + d_2 + \dots + d_{n-1} = a_n - a_0$.
- As proof, expand each $d_k$ using its definition, and watch all the terms magically cancel out!
  - This is known as a **telescoping** sum.
- So, if we have a nice formula for $d_0 + d_1 + d_2 + \dots + d_{n-1}$, then we will also have a nice formula for $a_n$
  - As an exercise, you can use this fact to show that if a sequence has a common difference (i.e. $d_n = c$ for all $n$), then $a_n = a_0 + cn$.

Let's examine the difference sequence of the Alice sequence.  We define the "difference sequence" $d_n = a_{n+1} - a_n$.
  
- If we compute the terms of $d$, we seem to get $1, 3, 5, 7, 9, \dots$  This isn't constant, but it is a familiar sequence---these _seem_ to be the positive odds!
- Let's formally prove that the difference sequence really is the odd numbers.
  - Recall that the Alice sequence is _defined_ by $a_{n+1} = 2\, a_{n} - a_{n-1} + 2$.
  - We can rearrange this to $(a_{n+1} - a_{n}) = (a_{n} - a_{n-1}) + 2$.
  - Substituting, we see then that $d_n = d_{n-1} + 2$.
  - We can alternately write this as $d_n - d_{n-1} = 2$.
    - The difference sequence _of the difference sequence_ is constant.
  - Thus, we have the formula $d_n = 1 + 2n$, which gives us the positive odds.

Given this formula for $d_n$, note that we now need a "clean" formula for the sum of the first $n$ positive odds.  Rather famously, the sum of the first $n$ positive odds is actually equal to $n^2$.  You can prove this by induction, or you can consider the neat visual proof shown below.

# TODO

Recall that $a_n = (d_0 + d_1 + \dots + d_{n-1}) + a_0$.  Substituting, we get the formula $a_n = n^2 + 2$, and we are done!

As a final remark, difference sequences turn out to be a very powerful tool in analyzing sequences and series.
- If the difference sequence is constant, then the original sequence is some _linear_ function.
- If the difference sequence _of a difference sequence_ is constant, then the original sequence is some _quadratic_ function.
- If you get a constant function after applying the "take the difference sequence" step $k$ times, then the original sequence can actually be shown to be a polynomial of degree $k$.
- Mathologer goes in depth into this concept in his video [here](https://www.youtube.com/watch?app=desktop&v=4AuV93LOPcE)
  - For the more advanced students reading this, the "gist" is that difference sequences are like a discrete version of the derivative!


</details>

