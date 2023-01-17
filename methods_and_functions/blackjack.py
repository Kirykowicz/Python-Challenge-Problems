# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(c1, c2, c3):
    input_array = [c1, c2, c3]
    card_sum = sum(input_array)
    if card_sum >= 21 and 11 in input_array:
        card_sum -= 10
        if card_sum >= 21:
            return 'Bust'
    elif card_sum >= 21 and not 11 in input_array:
        return 'Bust'
  
    return str(card_sum)

print(blackjack(10,11,11))

# alternate solution 

def blackjack_alternate(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return 'Bust'