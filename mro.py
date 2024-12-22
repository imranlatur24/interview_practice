class A:
    def a(self):
        print('a called ')
class B(A):
    def a(self):
        print('b called ')
class C(A):
    def a(self):
        print('c called ')
class D(B,A):
    pass

d=D()
d.a()