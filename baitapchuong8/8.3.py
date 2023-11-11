a = eval(input('Nhập a ='))
b = eval(input('Nhập b ='))
print('Phương trình bậc nhất : ', a,'x', '+', b)
if a == 0:
    print('Phương trình vô nghiệm')
elif a != 0:
    print('Phương trình có nghiệm', 'x', '=', -b / a)
elif b == 0:
    print('Phương trình vô số nghiệm')
else:
    print('Kết thúc bài toán')