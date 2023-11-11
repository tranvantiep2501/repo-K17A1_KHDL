a = eval(input('Loại xe :'))
b = eval(input('Số km :'))
c = eval(input('Thời gian chờ :'))
#Dành cho xe 4 chỗ
gia_mo_cua = 11000 * b
pv_20km = 12100 * b
km_21_trodi = 10000 * b 
tien_cho = 800 * (c - 5)
if c >= 6:
    print('Tiền chờ :', tien_cho, 'đồng')
else:
    print(0)
if a == 4:
    print('Giá mở cửa : ', gia_mo_cua, 'đồng')
elif b <= 20:
    print('Tiền di chuyển :', pv_20km, 'đồng')
    print('Tiền cước : ', tien_cho + pv_20km, 'đồng')
elif b >= 21:
    print('Tiền di chuyển :', km_21_trodi, 'đồng')
    print('Tiền cước :', tien_cho + km_21_trodi, 'đồng')
else: 
    print('tạm biệt')

#Dành cho xe 7 chỗ
gia_mo_cua1 = 13000 * b
pv_30km = 14100 * b 
km_31_trodi = 12000 * b
tien_cho1= 800 * (c - 5)
if c >= 6:
    print('Tiền chờ :', tien_cho1, 'đồng')
else:
    print('Không tính tiền chờ')

if a == 7:
    print('giá mở cửa :', gia_mo_cua1, ' đồng')
else:
    print('Tạm biệt')
if b <= 30:
    print('Tiền di chuyển :', pv_30km, 'đồng')
    print('Tiền cước :', tien_cho1 + pv_30km, 'đồng')
elif b >= 31:
    print('Tiền di chuyển :', km_31_trodi, ' đồng')
    print('Tiền cước :', tien_cho1 + km_31_trodi, 'đồng')
else:
    print('xong')