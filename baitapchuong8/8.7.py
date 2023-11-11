kwh = float(input('Nhập số Kwh tiêu thụ :'))
if kwh <= 50:
    print('Giá bán điện = ', 50 * 1.678, 'đồng')
elif kwh <= 100:
    print('giá bán điện =',  50 * 1.678 + (kwh - 50) * 1.734, 'đồng')
elif kwh <= 200:
    print('giá bán điện =', 50 * 1.678 + 50 * 1.734 + (kwh - 100) * 2.014, 'đồng')
elif kwh <= 300:
    print('giá bán điện = ', 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + (kwh - 200) * 2.536, 'đồng')
elif kwh <= 400:
    print('giá bán điện = ', 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 200 * 2.536 + (kwh - 300) * 2.834, 'đồng')
else:
    print('Giá bán điện = ', 50 * 1.678 + 50 * 1.734 + 100 * 2.014 + 200 * 2.536 + 300 * 2.834 + (kwh - 400) * 2.927, 'đồng')