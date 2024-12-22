
def editable_immumutable(x):
    x+=1
    #print('inside immutable value of x ',x)
    return x

def editable_mutable(lst):
    lst.append(4)
    return lst

# Call by value example
# primitive value[string,int,tuple etc] passed by value
x=1
print('before outside  immutable value of x ',x)
editable_immumutable(x)
print('after outside immutable value of x ',x)

# Call by reference example
# non-primitive value [list,set,dictionary] passed by refrence
lst=[1,2,3]
print('before outside mutable value of lst ',lst)
editable_mutable(lst)
print('after outside mutable value of lst ',lst)
