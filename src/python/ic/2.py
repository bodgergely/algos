

def get_products_of_all_ints_except_at_index(nums):
    def calc_product(l,r,nums, dic, is_left_side):
        prod = 1
        if l > r or r > len(nums)-1:
            return prod
        if l == r:
            prod = nums[l]
        else:
            if not (l, r) in dic:
                if is_left_side:
                    dic[(l,r)] = nums[r] * calc_product(l, r-1, nums, dic, is_left_side)
                else:
                    dic[(l,r)] = nums[l] * calc_product(l+1, r, nums, dic, is_left_side)
            prod = dic[(l,r)]
        return prod
            
    dic = dict()
    products = []
    for i in range(len(nums)):
        products.append(calc_product(0, i-1, nums, dic, True) * calc_product(i+1, len(nums)-1, nums, dic, False))
    return products

l = [1,7,3,4]
print get_products_of_all_ints_except_at_index(l)
