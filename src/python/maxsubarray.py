
def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    s = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        s = s + A[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = float('-inf')
    s = 0
    max_right = high
    for i in range(mid+1, high+1, 1):
        s = s + A[i]
        if s > right_sum:
            right_sum = s
            max_right = i
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])   # base case only one element
    else:
        mid = (low + high)/2
        (left_low, left_high, left_sum) =    find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


    
    
    

if __name__ == '__main__':
    l = [1,-2,7,-2, 8,-4,-6,9,-4]
    length = len(l)
    print find_maximum_subarray(l, 0, length-1)



