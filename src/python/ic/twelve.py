

def binary_search(elems, value):
    def bin_search(low, high, elems, value):
        if low == high:
            if elems[low] == value:
                return low
            else:
                return None
        if low > high:
            return None

        mid = (low + high) / 2
        if value == elems[mid]:
            return mid
        elif value < elems[mid]:
            return bin_search(low, mid-1, elems, value)
        else:
            return bin_search(mid+1, high, elems, value)

    return bin_search(0, len(elems)-1, elems, value)

if __name__ == '__main__':
    l = [5,2,98,34,37,23,76,7]
    l.sort()
    print l
    print binary_search(l, 98)
    
