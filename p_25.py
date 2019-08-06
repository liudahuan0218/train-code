class Capstr(str):
    def __new__(cls,string):
        string=string.upper()
        return super(Capstr,cls).__new__(cls,string)
    def __str__(self):
        print('ok')
a=Capstr('love')
b=Capstr('like')
