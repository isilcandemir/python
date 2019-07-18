def square(value):
    new_value = value**2
    return new_value
    
square(4)

y=square(4)
print(y)

def mod2plus5(x1, x2, x3):
    def inner(x):
        return x%2+5
    return(inner(x1), inner(x2), inner(x3))
    
raise_to_power=lambda x,y: x**y

map(lambda x: x**2, seq)

bebe=[1,2,3,4]
it=iter(bebe)
next(it)

bebe=[1,2,3,4]
new_bebe=[x+1 for x in bebe]

# [ output expression for iterator variable in iterable if predicate expression ]
