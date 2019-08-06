def A(a):
    def B(b):
        return a*b
    return B
C=A(2)
print(C(4))
