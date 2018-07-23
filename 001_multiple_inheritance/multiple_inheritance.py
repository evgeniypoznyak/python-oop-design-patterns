class A:
    def __init__(self):
        print('A')

    @staticmethod
    def foo():
        print('foo')


class B:
    def __init__(self):
        print('B')

    @staticmethod
    def bar():
        print('bar')


class C(A, B):
    def foobar(self):
        self.foo()
        self.bar()


c = C()

print(C.__mro__)

c.foobar()
