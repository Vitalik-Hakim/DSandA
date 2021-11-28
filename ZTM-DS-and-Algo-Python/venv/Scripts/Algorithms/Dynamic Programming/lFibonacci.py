import time


cache = {}

def dy_fib(n):
    if n in cache:
        return cache[n]
    else:
        if n<2:
            return n
        else:
            cache[n] = dy_fib(n-1) + dy_fib(n-2) 
            return cache[n]

t1 = time.time()
print(dy_fib(30))
t2 = time.time()
print(t2-t1)