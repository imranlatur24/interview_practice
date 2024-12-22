import copy
l2 = [[1,2],[3,4]] 
cp = copy.copy(l2)
cp[0][0] = 45
print(cp)
print(l2)

