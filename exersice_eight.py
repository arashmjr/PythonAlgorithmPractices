# Print the result of addition, subtraction, multiplication, division and modulus of complex numbers.

import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.imaginary * no.real + self.real * no.imaginary)

    def __truediv__(self, no):
        no_mod2 = float(no.real * no.real + no.imaginary * no.imaginary)
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / no_mod2,
                       (self.imaginary * no.real - self.real * no.imaginary) / no_mod2)

    def mod(self):
        return Complex(abs(complex(self.real, self.imaginary)), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


first_num = map(float, input('Enter The real and imaginary part of first number that separated by a space:').split())
second_num = map(float, input('Enter The real and imaginary part of second number that separated by a space:').split())


first_number_obj = Complex(*first_num)

second_number_obj = Complex(*second_num)

print(*map(str, [first_number_obj+second_number_obj,
                 first_number_obj-second_number_obj,
                 first_number_obj*second_number_obj,
                 first_number_obj/second_number_obj,
                 first_number_obj.mod(),
                 second_number_obj.mod()])
      , sep='\n')
