class Singleton(object):
  __instance =None
  def  __new__  (cls,age,name ):
  #如果类属性__instance的值为None,
  #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时能够知道之前已经创建过对象了，这样就保证了只有1个对象
     if not cls.__instance:
         cls.__instance =super().__new__ (cls)
     return (cls.__instance)
class A(Singleton):
    def __init__(self,s,m):
        self.s=s
a = A(18, "dongGe" )
b = A(8, "dongGe")
C = A(82, "dongGe")
print(id(a),a.s)
print(id(b),b.s)
print(id(C),C.s)
