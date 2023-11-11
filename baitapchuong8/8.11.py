a = int(input('Nhập n :'))
b = int(input('Nhập x :'))
c = (b * b + b + 1) ** a + (b * b - b + 1) ** a
print('A', '=', "(x * x + x + 1) ^n + (x * x - x + 1) ^n =", c)