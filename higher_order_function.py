fruits = ['apple','anjeer','banana']
mapli = map(lambda s:s[0]=='a',fruits)
print(list(mapli))

filli = filter(lambda s:s[0]=='a',fruits)
print(list(filli))

from functools import reduce
l = [1,2,3,4,5]
myr = reduce(lambda x,y:x+y,l)
print(myr)


s = lambda x:x*x*x
print(s(5))

lstf = lambda x:x%2==0,l
print(lstf)
