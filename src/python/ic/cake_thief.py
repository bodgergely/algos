
"""
type: dynamic programming - overlapping subproblems - approach: find the highest value cake if capacity is 1 then solve it for capacity 2 where we can use the max_value_at_1
problem - 16th 
the max value for each capacity value can be calculated by 
"""

def max_duffel_bag_value(cake_tuples, weight_capacity):
    max_value_at_capacities = [0] * (weight_capacity + 1)
    # We care about any cakes that weigh the current capacity or less. 
    for current_capacity in xrange(weight_capacity + 1):
        # go through all the cakes
        for cake_weight, cake_value in cake_tuples:
            # if the cake weighs as much or less than the current capacity
            # see what our max value could be if we took it!
            if cake_weight <= current_capacity:
                # find max_value_using_cake
                remaining_weight = current_capacity - cake_weight
                max_value_using_cake = max_value_at_capacities[remaining_weight] + cake_value
                max_value_at_capacities[current_capacity] = max(max_value_at_capacities[current_capacity], max_value_using_cake)

    return max_value_at_capacities[weight_capacity]
        


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)