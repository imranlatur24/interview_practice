def myfun(*args):
    total=0
    for i in args:
        total=total+i
    return total

print(myfun(1,2,3,4,5))