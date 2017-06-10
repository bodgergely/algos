

"""
type: Dynamic programming. Bottom-up approach. We keep updating a list where the index is the amount and the value is how many ways we can give change for that amount
by going from the first coin in the denominations and always updating by checking the nums ways to get ways[curr_amount-curr_coin] + ways[curr_amount]
we bootstrap the table by filling it up with zeros except the 0-th element which is 1 meaning we can give 0 amount in 1 way 
"""

def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]

amount = 4
denoms = [1,2,3]
print change_possibilities_bottom_up(amount, denoms)