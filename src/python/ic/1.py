
def calc_deltas(prices):
    l = []
    prev = prices[0]
    for p in prices:
        l.append(p - prev)
        prev = p
    return l

def get_max_profit(prices):
    deltas = calc_deltas(prices)    
    # we have the deltas now we have to find the subsequence that sums to the max
    # CLRS book - find max subarray problem - page 72
    def find_max_cross_sum(A, p, m, r):
        # [4,-3,8,1,-5]
        curr_sum = A[m]
        best_sum = curr_sum
        lp = m
        rp = m
        for i in range(m-1, p-1, -1):
            curr_sum += A[i]
            if curr_sum > best_sum:
                best_sum = curr_sum
                lp = i
        curr_sum = best_sum
        for i in range(m+1, r+1):
            curr_sum += A[i]
            if curr_sum > best_sum:
                best_sum = curr_sum
                rp = i
        return (lp,rp,best_sum)

    def find_max_seq(deltas, p, r):
        if p == r:
            return (p,r, deltas[p])
        m = (p + r) / 2
        (left_low, left_high, left_sum) = find_max_seq(deltas, p, m)
        (right_low, right_high, right_sum) = find_max_seq(deltas, m+1, r)
        (cross_low, cross_high, cross_sum) = find_max_cross_sum(deltas, p, m, r)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
        #[1,2,3,4,5,6]
        

    return find_max_seq(deltas, 0, len(deltas)-1)

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)