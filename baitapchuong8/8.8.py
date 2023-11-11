phong = int(input('Nhập loại phòng (từ 1 - 8) :'))
dem = int(input('Nhập số đêm :'))
if phong == 1:
    print('Đây là phòng Standard')
    if dem == 1:
        print('tiền phòng của bạn là ', dem * 1260000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là',  dem * 1260000 * 0.75, 'đồng')
    if dem > 4:
        print('tiền phòng của bạn là', dem * 1260000 * 0.7, 'đồng')
elif phong == 2:
    print('Đây là phòng Superior Garden View')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 1550000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 1550000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 1550000 * 0.7, 'đồng')
elif phong == 3:
    print('Đây là phòng Superior Ocean View')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 1830000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 1830000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 1830000 * 0.7, 'đồng')
elif phong == 4:
    print('Đây là phòng Garden View Bungalow')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 1830000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 1830000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 1830000 * 0.7, 'đồng')
elif phong == 5:
    print('Đây là phòng Garden Pool View Bungalow')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 2120000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 2120000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 2120000 * 0.7, 'đồng')
elif phong == 6:
    print('Đây là phòng Family Room')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 2120000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 2120000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 2120000 * 0.7, 'đồng')
elif phong == 7:
    print('Đây là phòng Beach Front Bungalow')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 2540000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 2540000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 2540000 * 0.7, 'đồng')
elif phong == 8:
    print('Đây là phòng VIP sea View')
    if dem == 1:
        print('Tiền phòng của bạn là', dem * 4800000, 'đồng')
    if dem == 2 or dem == 3:
        print('Tiền phòng của bạn là', dem * 4800000 * 0.75, 'đồng')
    if dem > 4:
        print('Tiền phòng của bạn là', dem * 4800000 * 0.7, 'đồng')