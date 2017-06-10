import random
import sys
import math

def swap(A, i, j):
    a = A[i]
    A[i] = A[j]
    A[j] = a

def randomize_in_place(A):
    n = len(A)
    for i in range(0, n):
        r = random.randint(i, n-1)
        swap(A, i, r)

def permute_with_all(A):
    n = len(A)
    for i in range(0, n):
        r = random.randint(0, n-1)
        swap(A, i, r)


def test_permutation_randomness(n):
    s = dict()
    l = [1,2,3,4,5,6,7,8,9,10]
    s[tuple(l)] = 1
    for i in range(n):
        permute_with_all(l)
        #randomize_in_place(l)
        #random.shuffle(l)
        if not s.has_key(tuple(l)):
            s[tuple(l)] = 1
        else:
            s[tuple(l)]+=1
    repetionCount = 0
    for k,v in s.iteritems():
        if v > 1:
            repetionCount+=1
    print repetionCount

def random_sample(m, n):
    if m == 0:
        return set()
    else:
        S = random_sample(m-1, n-1)
        i = random.randint(1, n)
        if i in S:
            S.add(n)
        else:
            S.add(i)
        return S
            
def prob_counting(bits, n, iters):    
    i = 0
    if iters >= len(n):
        iters = len(n) - 1
    for _ in range(iters):
        if i == math.pow(2, bits) - 1:
            raise OverflowError
        else:
            prob = 1.0 / (n[i+1] - n[i])
            if random.random() <= prob:
                i+=1
    return i

if __name__ == "__main__":
    l = [x for x in range(0, 100)]
    l2 = [math.pow(2,x) for x in range(0, 32)]
    print prob_counting(32, l2, len(l2))
    
            
        
