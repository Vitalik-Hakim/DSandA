#Getting it

def iterative_reverse(string): #Here we use a second string to store the reversed version. Time and Space complexity = O(n)
    reversed_string = ''
    for i in range(len(string)): # Loop 5 times
        reversed_string = reversed_string + string[len(string)-i-1] # "" + hello[5-h-1]
        print(reversed_string)
    #return reversed_string

print(iterative_reverse("Hello"))

#Now lets reverse a string through iteration


def reverse_iter(string):
    reverse_str = ''
    for i in range(len(string)):
        reverse_str = reverse_str + string[len(string)-i-1]
    return reverse_str

print(reverse_iter("Hakim"))


#Writing it the third time


def reverse_iter(k):
    reverse = ""
    for i in range(len(k)):
        reverse = reverse + k[len(k)-i-1]
    return reverse

print(reverse_iter("Bro"))




#writing it the fourth time


def i(k):
    r = ''
    for i in range(len(k)):
        r = r + k[len(k)-i-1]
    return r

print(i("Iamokayy"))



#Writing it the 5th time



def x(s):
    z = ''
    for i in range(len(s)):
        z = z + s[len(s)-i-1]
    return z


print(x("I am hakim"))



####
#Writing iteratively for 5 times again with a dif method
####



#Here we append the string backwards into the original string itself and then slice it to contain only the 2nd half,i.e.,the reversed part.
#Time complexity = O(n). Space complexity = O(n)
def second_iterative_reverse(string):
    original_length = len(string) # original_l = 5
    for i in range(original_length):# Loop five times 
        string = string + string[original_length - i - 1] # s = s + 5-letter-1
    string = string[original_length:] # s = s + original from start to end 
    return string

# 1st

def sir(string):
    org_l = len(string)
    for i in range(org_l):
        string = string + string[org_l -i -1]
    string = string[org_l:]
    print(string)
    return string
sir("Hello")



#2nd

def sec(stri):
    origi = len(stri)
    for i in range(origi):
        stri = stri + stri[origi-i-1]
    stri = stri[origi:]
    return stri

print(sec("Broo"))


# 3rd time


def o(s):
    d = len(s)
    for i in range(d):
        s = s + s[d-i-1]
    s = s[d:]
    return s
print(o("ahh"))




#4th time

def food(eat):
    how = len(eat)
    for i in range(how):
        eat = eat + eat[how-i-1]
    eat = eat[how:]
    return eat

print(food("banku"))






# 5th time

def y(x):
    z = len(x)
    for i in range(z):
        x = x + x[z-i-1]
    x = x[z:]
    return x

print(y("Math"))



# 6th time for fun


def a(b):
    c = len(b)
    for i in range(c):
        b = b + b[c-i-1]
    b = b[c:]
    return b

print(a("Donee"))


# Just curious does it work with intergers though?


def n(x):
    n1 = len(x)
    for i in range(n1):
        x = x + x[n1-i-1]
    x = x[n1:]
    return x

num = print(n("1233")) # Sike it doesn't! looks like we have to convert it back after doing it






def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


# 1st time


def rr(s):
    if len(s) == 0:
        return s
    else:
        return rr(s[1:]) + s[0]

print(rr("Brov"))




# 2nd time



def so(s):
    if len(s) == 0:
        return s
    else:
        return so(s[1:]) + s[0]


print(so("Soose"))



# 3rd time


def g(a):
    if len(a) == 0:
        return a
    else:
        return g(a[1:]) + a[0]

print(g("SFGDFJCNGDJ"))


# 4th time

def gee(c):
    if len(c) == 0:
        return c
    else:
        return gee(c[1:]) + c[0]

print(gee("NEWASIKNA"))



# 5th Time

def to(by):
    if len(by) == 0:
        return by
    else:
        return to(by[1:]) + by[0]

print(to("I am done with this thing"))






























































        