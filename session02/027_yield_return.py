def generate_squares_yield(n):
    for i in range(n):
        yield i 

def generate_squares_return(n):
    for i in range(n,15):
        return i 

g = generate_squares_yield(5)
h = generate_squares_return(5)

print (list(g))
print (generate_squares_return(5))