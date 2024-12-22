class A:
    def a(self):
        print('a class called')
class B(A):
    def b(self):
        print('b class called')
    
ba = B()
ba.a()
ba.b()