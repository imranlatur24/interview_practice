#before sorrt [3, 24, 1, 2, 96, 0, 34]
#after sorrt [0, 1, 2, 3, 24, 34, 96]
mylist=[3, 24, 1, 2, 96, 0, 34]
print('before sort ',mylist) 
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i]>mylist[j]:
            mylist[i],mylist[j] = mylist[j],mylist[i]
print('after sort ',mylist)