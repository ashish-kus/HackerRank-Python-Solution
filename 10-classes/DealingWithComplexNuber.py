import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def __add__(self, no):
        a = self.real + no.real
        b = self.imag + no.imag
        return Complex(a, b)
        
    def __sub__(self, no):
        a = self.real - no.real
        b = self.imag - no.imag
        return Complex(a, b)
        
    def __mul__(self, no):

        realPart = ((self.real * no.real) - (self.imag * no.imag))
        imagPart = ((self.real * no.imag) + (self.imag * no.real))
        return Complex(realPart, imagPart)
        
    def __truediv__(self, no):
        no2 = no
        no2.imag = (-1)* no2.imag
        num = self * no2
        denom = no.real**2 + no.imag**2
        return Complex(num.real / denom, num.imag / denom)
        

    def mod(self):
        realPart = round(((self.real**2) + (self.imag**2))**0.5, 2)
        imagPart = 0
        return Complex(realPart, imagPart)
        
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
