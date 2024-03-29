def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(love):
    print ("hello {}!".format(love))
