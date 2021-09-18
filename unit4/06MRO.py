
class A:
    def __init__(self):
        super().__init__()
        print('A.init')
        self.a = 'a'

    def foo(self):
        print(f'now at A')
        #super().foo()
        print(f'a {self.a}')
        print(f'now at A')

class A1:
    def __init__(self):
        super().__init__()
        print('A1.init')
        self.a1 = 'a1'

    def foo(self):
        print(f'now at A1')
        #super().foo()
        print(f'a1 {self.a1}')
        print(f'now at A1')


class B1(A,A1):
    def __init__(self):
        super().__init__()
        print('B1.init')
        self.b1 = 'b1'

    def foo(self):
        print(f'now at B1')
        super().foo()
        print(f'b1 {self.b1}')
        print(f'now at B1')

x=B1()
x.foo()


class B(A):
    def __init__(self):
        super().__init__()
        print('B.init')
        self.b = 'b'

    def foo(self):
        print(f'now at B')
        super().foo()
        print(f'b {self.b}')
        print(f'now at B')



class C(A):
    def __init__(self):
        super().__init__()
        print('C.init')
        self.c = 'c'

    def foo(self):
        print(f'now at C')
        super().foo()
        print(f'c {self.c}')
        print(f'now at C')



class D(B,C):
    def __init__(self):
        super().__init__()
        print('D.init')
        self.d = 'd'

    def foo(self):
        print(f'now at D')
        super().foo()
        print(f'd {self.d}')
        print(f'now at D')


d = D()
d.foo()
print(d.d)
