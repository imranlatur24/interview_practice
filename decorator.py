def decor_fun(func):
    print('main fun worked')
    def wrapper_fun():
        print('wrapper worked')
        return func
    return wrapper_fun()
def show():
    print('show worked')

decor_show = decor_fun(show)
decor_show()

print('-----------')
@decor_fun
def disp():
    print('display worked')
disp()