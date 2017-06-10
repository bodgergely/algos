

def merge_ranges(intervals):
    def merge(left_start, left_end, right_start, right_end):
        start = left_start
        if left_end >= right_end:
            return (start, left_end)
        else:
            return (start, right_end)

    def merge_two(left, right):
        print "left:" , left 
        left_start, left_end = left
        right_start, right_end = right
        
        if right_start > left_end:
            return ([left,right], False)
        else:
            merged = merge(left_start, left_end, right_start, right_end)
            return (merged, True)
    
    merged_list = []
    intervals = sorted(intervals, key=lambda x:x[0])
    print "sorted: ", intervals
    current = intervals[0]
    for i in range(1, len(intervals)):
        print "To be merged: ", current, intervals[i]
        merged = merge_two(current, intervals[i])
        print "merged: ", merged
        if merged[1] == False:
            left, right = merged[0]
            merged_list.append(left)
            current = right
        else:
            current = merged[0]
    merged_list.append(current)

    return merged_list

l = [(0, 1), (4, 8), (3, 5), (10, 12), (9, 10)]
print merge_ranges(l)

