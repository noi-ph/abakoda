## Joker

<details closed>
<summary>Hint 1</summary>

Suppose there are $k$ jokers in the hand.  What is the minimum possible value that you can make the final hand have?  How about the maximum possible value?

</details>

<details closed>
<summary>Hint 2</summary>

Is it possible for you to make the hand take on every value between the minimum and maximum?  Can you prove this?

</details>

<details closed>
<summary>Solution</summary>

Suppose the hand has $k$ jokers, and the fixed non-joker cards have a total value of $\text{total}$.  Then, the minimum possible value is $\text{total} + k$ if we replace all jokers with aces, and the maximum possible value is $\text{total} + 10k$ if we replace all jokers with tens (or face cards).

Let's prove that we can make the final hand take on any value from $\text{total} + k$ all the way to $\text{total} + 10k$.  Start by replacing all jokers with aces.  Then, we can repeatedly apply the following "increment" operation.

- Choose a card that used to be a joker, and whose value is less than $10$; replace it with a card whose value is $+1$ higher.

Every time we apply this operation, the total value of the hand increases by $+1$.  And we can keep applying this operation until the total value of the hand is maximum possible (when all the jokers have been replaced with tens).  Since we traveled from the min to the max using only these $+1$ increments, that means we must have encountered a solution to every integer value in between, along the way.

We can directly translate this idea into a constructive algorithm.

- First, set all jokers to aces.
- Until the total value of the hand has become the desired value, find a non-maximized joker and apply the $+1$ increment operation to it.  Repeat as many times as necessary.
  
This gives us an $\mathcal{O}(n + 10n)$ solution, since the maximum value of any card is $10$.

With a few tweaks, this solution can be made to run in $\mathcal{O}(n)$, regardless of the maximum value of a card.  You can think about how you might be able to achieve this optimization (it's not hard), but it's not necessary to get an Accepted for J.

</details>

<details closed>
<summary>Bonus</summary>

In Blackjack, an ace can take on the value of $1$ or $11$ (your choice).  Suppose that aces are encoded as `@`, and---in addition to dealing with the jokers---you must also replace each `@` with `a` (for a value of $1$) or `A` (for a value of $11$).

Now, which total values can we construct for the final hand, and how?
</details>