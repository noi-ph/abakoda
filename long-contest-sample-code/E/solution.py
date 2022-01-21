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
