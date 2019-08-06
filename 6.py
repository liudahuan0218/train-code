class A:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
        print('init')
    def mydefault(self,*args):
        print('default:',str(args[0]))
    def __getattr__(self,name):
        print('other fn:',name)
        return self.mydefault
a=A(10,20)
a.fn1(33)
a.fn2('hello')
a.fn3(10)
