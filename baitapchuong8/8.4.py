import math


a = float(input('Nhập cạnh a ='))
b = float(input('Nhập cạnh b ='))
c = float(input('Nhập cạnh c ='))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Nửa chu vi = ', p)
print('Diện tích tam giác = ', s)