# Menu chọn bài tập
def menu():
    while True:
        print('Chọn bài tập bạn muốn xem bằng cách nhập số đầu mục tương ứng')
        print('1. Bài 1: In ra dãy số từ . . . đến . . . với bước số')
        print('2. Bài 2: Tính tổng của các số chẵn/lẻ')
        print('4. Bài 4: Đếm số từ trong một câu được nhập')
        print('3. Thoát')
        choice = int(input('Mời chọn: '))

        if choice == 1:
            bai_1()
        elif choice == 2:
            bai_2()
        elif choice == 4:
            bai_4()
        elif choice == 3:
            break
        else:
            print('Không hợp lệ, mời nhập lại!\n')
            menu()

def bai_1():
    number = int(input('Nhập số bạn muốn in cả dãy số ra màn hình: '))
    start_num = int(input('Nhập số bắt đầu in: '))
    distance = int(input('Nhập khoảng cách giữa các số trong dãy: '))

    in_ra_man_hinh(number, start_num, distance)


def in_ra_man_hinh(n,i,step):
    while i <= n:
        print(i, end=' ')
        i += step

def bai_2():
    number = int(input('Nhập số cuối: '))
    start_num = int(input('Nhập số đầu: '))
    type = input('Nhập chữ "chan" hoặc "le": ')

    print(tinh_tong(number, start_num, type))

def tinh_tong(n,i,type):
    tong = 0
    while i <= n:
        if type == 'chan':
            if i % 2 == 0:
                tong = tong + i
                print(f'{i} +', end=' ')
            i += 1
        elif type == 'le':
            if i % 2 > 0:
                tong = tong + i
                print(f'{i} +', end=' ')
            i += 1
        else:
            print('Kiểu số không hợp lệ!')
            break

    return tong

def bai_4():
    chuoi = input('Nhập câu bạn muốn đếm số từ: ')
    words = chuoi.split()
    print(f'Chuỗi có {len(words)} từ: ', end=' ')
    print(f'{words}\n')

# Chạy chương trình
menu()
