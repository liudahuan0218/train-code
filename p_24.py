class animal():
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello,i am %s'%self.name)
class dog(animal):
    def greet(self):
        super(dog,self).greet()
        print('wangwang')
