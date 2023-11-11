a = float(input('Lãi suất 1 năm (%) : '))
b = int(input('Số tiền gửi : '))
c = int(input('Số tháng gửi : '))
tien_lai = (b * c) * (a / 12)
von_cong_lai = b + tien_lai
print('Tiền lãi = ', tien_lai)
print('Tiền vốn + lãi = ', b, '+', tien_lai, '=', von_cong_lai)