num=9
def f1():
    global num
    num=20
def f2():
    print(num)
f2()
f1()
f2()
