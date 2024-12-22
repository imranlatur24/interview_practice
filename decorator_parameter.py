def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def operator(func,a,b):
    return func(a,b)

print(operator(add,10,20))
print(operator(sub,10,200))