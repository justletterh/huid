from random import randint as fakerandint
from random import choice

def list_str(l):
    o=[]
    for i in l:
        o.append(str(i))
    return o

def to_digits(n, b):
    digits=[]
    while n>0:
        digits.insert(0,n%b)
        n=n//b
    return digits

def from_digits(digits, b):
    n=0
    for d in digits:
        n=b*n+d
    return n

def to_l(s):
    o=[]
    for c in s:
        o.append(c)
    return o

def dupe(i,x):
    o=[]
    for n in range(x):
        o.append(i)
    return o

def randint(a,b):
    return choice([fakerandint(a,b),fakerandint(a,b),fakerandint(a,b)])