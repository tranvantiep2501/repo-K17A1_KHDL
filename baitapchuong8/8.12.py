a = eval(input('Nhập một số x :'))
if a % 1 == 0 and a % a == 0:
    print(a, 'là số nguyên tố')
else:
    print(a, 'không phải là số nguyên tố')