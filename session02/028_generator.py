import random

def cube(n):
    for i in range(n):yield i ** 3

def odd(n):#impar
    for i in range(n):
        if i % 2 != 0:
            yield i

def even(n):#par
    n=int(n)
    for i in range(n):
        if i % 2 == 0:
            yield i

def random_list(n,min,max):
    for i in range(n):
        yield random.randint(min,max)

print (list(cube(5)))
print (list(odd(10)))
print (list(even(10.9)))
print (list(randomlist(10,0,100)))