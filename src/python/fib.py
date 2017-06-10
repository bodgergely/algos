
import sys
import matplotlib.pyplot as plt

def fib(n):
    fib.counter+=1
    if n == 0:
      return 0
    elif n == 1:
      return 1
    else:
      return fib(n-1) + fib(n-2)


fib.counter = 0
fib_mem.counter = 0

def plot(n, fun):
    x = []
    y = []
    for i in range(n):
        fun.counter = 0 
        x.append(i)
        fun(i)
        y.append(fun.counter)
    plt.plot(x,y)
    plt.show()

def test(n):
    for i in range(n):
        assert(fib(i) == fib_mem(i))

if __name__ == '__main__':
    fib_mem(6)
    #test(18)
    #n = int(sys.argv[1])
    #plot(n, fib)
    #plot(n, fib_mem)
