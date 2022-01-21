def card_to_value(card):
    if card == '*':
        return 0
    elif card == 'A':
        return 1
    elif card in ['T', 'J', 'Q', 'K']:
        return 10
    else:
        return int(card)

# Always returns T for 10
value_order = '*A23456789T'
def value_to_card(value):
    return value_order[value]

n, m = map(int, input().split())
hand = list(input())

jokers = [
    i
    for i in range(n)
    if hand[i] == '*'
]

total_value = sum(card_to_value(card) for card in hand)

if total_value + len(jokers) <= m <= total_value + 10*len(jokers):
    print("YES")

    def increment(i):
        global total_value
        hand[i] = value_to_card(card_to_value(hand[i]) + 1)
        total_value += 1

    for joker in jokers:
        increment(joker)

    for joker in jokers:
        while total_value < m and hand[joker] != 'T':
            increment(joker)

    print(''.join(hand))

else:
    print("NO")
