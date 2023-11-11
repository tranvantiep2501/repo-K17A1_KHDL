a = eval(input('năm :'))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, 'là năm nhuận')
else:
    print(a, 'là năm không nhuận')
