class complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, c):
        self.real += c.real
        self.imag += c.imag
        return self

def wrapper(func):
    def abs(a, b):
        c = func(a, b)
        ret = c.real **2 + c.imag **2
        return ret
    return abs

@wrapper
def complex_add(complex1, complex2):
    return complex(complex1.real + complex2.real,complex1.imag + complex2.imag)
    
        
if __name__ == '__main__':
    a1 = complex(1,2)
    a2 = complex(3,4)
    print(complex_add(a1,a2))
    a3 = a1 + a2
    print('%d + %di'% (a3.real, a3.imag))