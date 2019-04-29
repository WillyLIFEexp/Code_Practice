# Challeng from Daily-Coding Problem
# Implement the following code, and create two function, car and cdr.
# car function should return the left side of the input
# cad function should return the right side of the input.
# example:
# Input : car(cons(3,4))
# Output : 3
# Input : cdr(cons(3,4))
# Output : 4

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

print(type(3,4)) # this will return as function type.
                 # inside of cons, we are still missing a function.

# Input a funciton
def car(function):
    # create a function
    def left(a,b):
        return a
    # input the newly created function to the original function.
    return function(left)

def cdr(a,b):
    def right(a,b):
        return b
    return function(right)

print(car(cons(3,4)))
print(cdr(cons(3,4)))

