def Fibonacci(n):
            
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 3:
            a = 1
            b = 1
            for i in range(n):
                
                a,b = b,a+b
        return a

