## Experiment - Pokemon Edition!

<details closed>
<summary>48 points</summary>

First, some prep work.  Consider each of the $171$ possible type combinations that a Pokemon could have.  For each such combination, attack it with all $18$ types, and record the type effectiveness of each attacking type against that type combination.  Let's call this set of type effectiveness responses the **fingerprint** of a type combination (you can check that all type combiantions yield distinct fingerprints).

Now, for each test case, attack the mystery Pokemon with all $18$ types, and record the judge's response for the type effectiveness of each attack---this is the fingerprint of the mystery Pokemon!  The answer will be the type combination in our database that bears this same fingerprint.

</details>

<details closed>
<summary>92 points</summary>

We don't need to attack with all $18$ types.  We just need to choose some subset of attacking types such that every possible type combination gives a distinct set of fingerprints, if we restrict ourselves to only attacking with those types.  Let's call such a subset _discriminating_.

How do we find a discriminating subset?  Well, don't try to work it out by hand.  You have a computer, so use it!
- Consider all $1$-element subsets of the attacking types.  Then, all $2$-element subsets, and then the $3$-element subsets, and so on.
- For each one, generate the fingerprints of all $171$ type combinations.
- If all fingerprints are distinct, then you have a discriminating subset!

This exhaustive search will show that the smallest discriminating subsets have $7$ elements in them.  For example, you can verify that `Fighting Flying Poison Ghost Steel Electric Fairy` works.  This is enough to get us $92$ points!

</details>

<details closed>
<summary>Solution</summary>

The $92$ point solution reveals a key insight.  If we always use the same fixed attack queries, then we will need at most $7$ attacks to discriminate between each possible type combination.  So, if we are to improve on that in any way, we must leverage the interactive nature of our problem and have our logic **adapt**.  When deciding on the next attack query, we should also take into account the _previous_ judge responses.

Many heuristic solutions will be able to pass, which use some kind of rule of thumb to determine what move to make at each next step.  For example, a minimax algorithm could work, or some other algorithm which assigns scores or weights to different types.

This solution sketch will detail a complete exhaustive brute force solution.  The benefit of this approach is that we can definitively _prove_ that $5$ queries is always going to be enough (because we checked everything!).

What we want is something like a _flowchart_.
- The flowchart begins with us in a box that contains some type that we should attack with.
- Attack the mystery Pokemon with that type, and receive a response from the judge.  The response can be one of $6$ different results.
- Six outgoing arrows branch out from the box that we are on, with each arrow labeled with a type effectiveness result.  Each arrow then leads to some other box in the flowchart.
- Follow the arrow that matches the response given by the judge, leading us to another box.
  - If we were led to a box that also contains a type and has six outgoing arrows that branch out to other boxes, then we repeat these steps.
  - Or, if the box has no outgoing arrows, then we are done, and the value in the box is our final answer.

Here is how we can create such a flowchart.  Let's define the following.
- Let `candidates` be a list of type combinations that makes up our search space, i.e. we are sure that the answer is _something_ in this list.  Of course, before any queries have been made, `candidates` contains all $171$ type combinations.  But as we get more information from queries, we can keep narrowing and narrowing our search space until it only contains one element (which we are then sure is the answer).
- Let the function `generate_decision_tree(candidates, q)` attempt to generate a flowchart that discriminates between all type combinations in `candidates`, using **only** at most $q$ queries.  
  - If such a flowchart does not exist, it returns `None` instead.

Now, how does `generate_decision_tree(candidates, q)` work?
- First, we should decide what value to put in our starting box.
  - If `candidates` is empty, then no type combination would yield this series of responses.
    - If we arrived here, then the judge must have been mistaken or lying.
  - If `candidates` only contains one element, then we can make this a "final answer" box and stop, because we know the final answer must be that one element left in the search space.
  - If `candidate` has at least two items, and `q = 0`, then the answer is `None`, because we would have needed at least one query to discriminate between the two type combinations in our search space.
  - Otherwise, we are going to attack the mystery Pokemon, and the value in this box will be the attacking type.
- But what type should we attack with?  Try all possible attacking types!
  - Consider some type `attacking_type`.
    - For each type combination in `candidates`, consider what would happen if it would be attacked with `attacking_type`.
    - There are six possible type effectiveness results.  We can _partition_ `candidates` into six smaller lists, where we group together all the types that have the same type effectiveness result from `attacking_type`.
    - The _actual_ response of the judge would tell us which of these six lists contains the true answer.
      - If, for example, the judge answers `1`, then we throw away all the elements of `candidates` except for those in the `1` partition.
      - We are now stuck with a recursive subproblem---we need to discriminate between all the elements in this partition, using $q-1$ queries.
  - In summary, do the following for each possible `attacking_type`.
    - Partition all type combinations in `candidates` into six groups, depending on the type effectiveness if that type combination is hit by `attacking_type`.
    - Recursively call `generate_decision_tree(partition, q-1)` on each of the six partitions.
      - If _all_ of these calls were successful, then this is good!
      - Put `attacking_type` in the box, and let the arrows from this box leads to the flowcharts generated by each of the partitions.
  - If this step failed for all possible `attacking_type`, then return `None`, because this must be impossible.

An exhaustive search is feasible because we only need to explore $18 \times 18 \times 18 \times 18 \times 18 \approx 1.9 \times 10^6$ different possibilities (and it only goes this deep because we immediately cut off any solutions that try to do more than $5$ attack queries).  The amount of work done for the partitioning in each of these possibilities is roughly $\mathcal{O}(|\text{candidates}|)$, but note that $|\text{candidates}| \leq 171$, and in many cases it's probably going to be a lot smaller than that.  Since $18^5 \times 171 \approx 3.2 \times 10^8$, our exhaustive search should definitely finish within the generous 10 second Time Limit.

For a bonus optimization, rather than maintaining an integer `q` (for the number of queries left), we can have some set called `used_attacks` as an argument instead.  If we track which attacks we've already used in a previous query on this branch, then we can avoid checking duplicate attacks.  The number of possibilities becomes only $18 \times 17 \times 16 \times 15 \times 14 \approx 10^6$, which should roughly halve our program's running time!

The nice thing about this approach is that **we only have to generate the flowchart once**, at the start of the program.  After that, we answer every query by just following the instructions in the flowchart that we created.

<details closed>
<summary>Unnecessary Optimization</summary>

Recall that we said that we can answer queries at lightning speed because we only need to generate the flowchart _once_.  Then, we can recycle it and use that same flowchart to answer all the queries.

But every time we run our program, we will always end up generating the same flowchart each time anyway.  So... what if you generate the flowchart _on a completely separate program_.  Then, serialize the created flowchart into a string so that it can be **hard-coded** into your submission!

We are cheating by making it so that the expensive exhaustive search is not counted towards the Time Limit in the online judge.  Instead, all our program has to do is parse the hard-coded flowchart, and then proceed to answer all the queries.

With this approach, even a not-that-optimized Python solution can answer all $980$ test cases in less than $200$ milliseconds.

The author thought that this solution, while funny, was a bit much to ask for.  Thus, the time limit was set to an incredibly lenient $10$ seconds.

</details>

</details>

<details closed>
<summary>Setter's Code (Python)</summary>

```py
from functools import reduce
from itertools import chain, combinations

raw_all_pkmn_types = 'Normal Fighting Flying Poison Ground Rock Bug Ghost Steel Fire Water Grass Electric Psychic Ice Dragon Dark Fairy'
raw_matchup_table = '''
1	1	1	1	1	0.5	1	0	0.5	1	1	1	1	1	1	1	1	1
2	1	0.5	0.5	1	2	0.5	0	2	1	1	1	1	0.5	2	1	2	0.5
1	2	1	1	1	0.5	2	1	0.5	1	1	2	0.5	1	1	1	1	1
1	1	1	0.5	0.5	0.5	1	0.5	0	1	1	2	1	1	1	1	1	2
1	1	0	2	1	2	0.5	1	2	2	1	0.5	2	1	1	1	1	1
1	0.5	2	1	0.5	1	2	1	0.5	2	1	1	1	1	2	1	1	1
1	0.5	0.5	0.5	1	1	1	0.5	0.5	0.5	1	2	1	2	1	1	2	0.5
0	1	1	1	1	1	1	2	1	1	1	1	1	2	1	1	0.5	1
1	1	1	1	1	2	1	1	0.5	0.5	0.5	1	0.5	1	2	1	1	2
1	1	1	1	1	0.5	2	1	2	0.5	0.5	2	1	1	2	0.5	1	1
1	1	1	1	2	2	1	1	1	2	0.5	0.5	1	1	1	0.5	1	1
1	1	0.5	0.5	2	2	0.5	1	0.5	0.5	2	0.5	1	1	1	0.5	1	1
1	1	2	1	0	1	1	1	1	1	2	0.5	0.5	1	1	0.5	1	1
1	2	1	2	1	1	1	1	0.5	1	1	1	1	0.5	1	1	0	1
1	1	2	1	2	1	1	1	0.5	0.5	0.5	2	1	1	0.5	2	1	1
1	1	1	1	1	1	1	1	0.5	1	1	1	1	1	1	2	1	0
1	0.5	1	1	1	1	1	2	1	1	1	1	1	2	1	1	0.5	0.5
1	2	1	0.5	1	1	1	1	0.5	0.5	1	1	1	1	1	2	2	1
'''

all_pkmn_types = raw_all_pkmn_types.split()
matchup_table = [
    [
        float(matchup)
        for matchup in row.split()
    ]
    for row in raw_matchup_table.strip().split('\n')
]

get_type_index = {
    pkmn_type: i
    for i, pkmn_type in enumerate(all_pkmn_types)
}

class Pokemon:
    # In Python 3.9+, just use "list" for type annotations
    #  without needing to import "List" from typing
    from typing import List
    types: List[str]

    def __init__(self, types: List[str]):
        self.types = sorted(types)

    def attacked_by(self, attacking_type: str) -> float:
        return reduce(
            lambda x, y: x*y,
            (
                matchup_table[get_type_index[attacking_type]][get_type_index[defending_type]]
                for defending_type in self.types
            )
        )

    def output_types(self) -> str:
        return '/'.join(self.types)

all_pkmn_type_combos = [
    Pokemon(pkmn_types)
    for pkmn_types in chain(*(
        combinations(all_pkmn_types, k)
        for k in [1, 2]
    ))
]

possible_results = [4, 2, 1, 0.5, 0.25, 0]

'''
This returns None if no decision tree exists which can 
 discriminate between all candidates, using the
 remaining number of queries
'''
MAGIC_LIMIT = 5
def generate_decision_tree(candidates, used_attacks):
    if len(candidates) == 0:
        return ({}, 'Liar!')  # No solution
    if len(candidates) == 1:
        return ({}, candidates[0].output_types())
    if len(used_attacks) == MAGIC_LIMIT:
        return None
    
    for attacking_type in all_pkmn_types:
        if attacking_type not in used_attacks:
            partitions = {
                result: []
                for result in possible_results
            }
            for pkmn in candidates:
                partitions[pkmn.attacked_by(attacking_type)].append(pkmn)

            decision_branches = {
                result: generate_decision_tree(
                    partition,
                    used_attacks | {attacking_type}
                )
                for result, partition in partitions.items()
            }

            if all(
                branch is not None
                for branch in decision_branches.values()
            ):
                return (decision_branches, attacking_type)
            
    return None
    
decision_tree, initial_attack = generate_decision_tree(all_pkmn_type_combos, set())

def query(attacking_type):
    print(f'ATTACK {attacking_type}', flush=True)
    return float(input())

for _ in range(int(input())):
    current_node, current_query_type = decision_tree, initial_attack
    while current_node != {}:
        current_node, current_query_type = current_node[query(current_query_type)]
    
    print(f'ANSWER {current_query_type}')
    assert(input() == 'YES')

```

</details>
