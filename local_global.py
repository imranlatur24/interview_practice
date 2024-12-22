x=100
def inner():
    global x
    print(x)
    x=10
    print('local ',x)

inner()
