#Given a number, we have to return its factorial.
#For example, factorial(5) should return 5! = 5*4*3*2*1 = 120
#We can solve this recursively, or iteratively.
#First we are going to solve it iteratively.




#sOLVING IT iteratively

def iter(n):
    f = 1
    for i in range(1, n+1): 
        f  = i*f
    return f

print(iter(5))


# Lets do it recursively


def recur(n):
    if n <= 1:
        return 1
    else:
        return n*recur(n-1)
print(recur(5))

#Adding numbers

def recure(n):
    if n <= 0:
        return 1
    return n + recure(n-1)
print(recure(5))