
""" type: GREEDY
    there might be negative numbers too, so we should find either
    the three largest 
    all three positive numbers
    2 negative and one positive

"""

def highest_product_from_any_three_ints(nums):
    highest_prod_3 = nums[0]
    highest_prod_2 = nums[0]
    highest = nums[0]
    lowest_prod_2 = nums[0]
    lowest = nums[0]

    for current in nums[1:]:
        if current * highest_prod_2 > highest_prod_3:
            highest_prod_3 = current * highest_prod_2
        elif current * lowest_prod_2 > highest_prod_3:
            highest_prod_3 = current * lowest_prod_2

        if current >= 0:
            if (current * highest > highest_prod_2):
                highest_prod_2 = current * highest
            if current * lowest < lowest_prod_2:
                lowest_prod_2 = current * lowest
        else:
            if (current * lowest > highest_prod_2):
                highest_prod_2 = current * lowest
            if current * highest < lowest_prod_2:
                lowest_prod_2 = current * highest

        if current > highest:
            highest = current
        if current < lowest:
            lowest = current
        
    return highest_prod_3
        
nums = [1, 10, -5, 1, -100]
print highest_product_from_any_three_ints(nums)