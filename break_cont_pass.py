for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')
print()

for i in range(1,11):
    if i==5:
        continue
    print(i)

def myfun():
    print('pass called')
    pass
myfun()