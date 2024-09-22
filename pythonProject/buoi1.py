# Menu chọn bài tập
def menu():
    while True:
        print('=== Chọn bài tập bạn muốn xem bằng cách nhập số đầu mục tương ứng ===')
        print('1. Mục 2 - Bài 1: In ra dãy số từ . . . đến . . . với bước số')
        print('2. Mục 2 - Bài 2: Tính tổng của các số chẵn/lẻ')
        print('3. Mục 4 - Bài 3: Kiểm tra chuỗi Palindrome')
        print('4. Mục 4 - Bài 4: Đếm số từ trong một câu được nhập')
        print('5. Mục 5 - Bài 5: Tính giai thừa')
        print('6. Mục 5 - Bài 6: Kiểm tra số nguyên tố')
        print('7. Mục 1, 6 - Bài 7: Thử try . . . catch . . . raise')
        print('8. Mục 3 - Bài 8: Quản lý học viên')
        print('87. Thoát')
        choice = int(input('Mời chọn: '))

        if choice == 1:
            bai_1()
        elif choice == 2:
            bai_2()
        elif choice == 3:
            bai_3()
        elif choice == 4:
            bai_4()
        elif choice == 5:
            bai_5()
        elif choice == 6:
            bai_6()
        elif choice == 7:
            bai_7()
        elif choice == 8:
            import quan_ly_hoc_vien
            quan_ly_hoc_vien.main()
        elif choice == 87:
            exit('Thoát chương trình!')
        else:
            print('Không hợp lệ, mời nhập lại!\n')
            menu()

"""Bài 1"""
def bai_1():
    number = int(input('Nhập số bạn muốn in cả dãy số ra màn hình: '))
    start_num = int(input('Nhập số bắt đầu in: '))
    distance = int(input('Nhập khoảng cách giữa các số trong dãy: '))

    in_ra_man_hinh(number, start_num, distance)

# In dãy số ra màn hình
def in_ra_man_hinh(n,i,step):
    while i <= n:
        print(i, end=' ')
        i += step

    print('\n')

"""Bài 2"""
def bai_2():
    number = int(input('Nhập số cuối: '))
    start_num = int(input('Nhập số đầu: '))
    type = input('Bạn muốn tính tổng các số chẵn hay lẻ. Nhập chữ "chan" hoặc "le": ')

    tong, so_hang = tinh_tong(number, start_num, type)
    print(f'{so_hang[3:]} = {tong}')

# Tính tổng các phần tử trong dãy số
def tinh_tong(n,i,type):
    tong = 0
    phep_tinh = ""
    while i <= n:
        if type == 'chan':
            if i % 2 == 0:
                tong = tong + i
                phep_tinh = phep_tinh + ' + ' + str(i)
            # i += 1
        elif type == 'le':
            if i % 2 > 0:
                tong = tong + i
                phep_tinh = phep_tinh + ' + ' + str(i)
            # i += 1
        else:
            print('Kiểu số không hợp lệ!')
            break

        i += 1

    return list((tong, phep_tinh))

"""Bài 3"""
def bai_3():
    # Nhập chuỗi từ người dùng
    input_string = input("Nhập chuỗi để kiểm tra: ")

    # Kiểm tra và in kết quả
    if is_palindrome(input_string):
        print(f'"{input_string}" là một chuỗi palindrome.\n')
    else:
        print(f'"{input_string}" không phải là một chuỗi palindrome.\n')

# kiểm tra chuỗi palindrome
def is_palindrome(s):
    s = s.replace(" ", "").upper()
    # So sánh chuỗi với chuỗi đảo ngược của nó
    return s == s[::-1]

"""Bài 4"""
def bai_4():
    chuoi = input('Nhập câu bạn muốn đếm số từ: ')
    words = chuoi.split()
    print(f'Chuỗi có {len(words)} từ: ', end=' ')
    print(f'{words}\n')

"""Bài 5"""
def bai_5():
    giai_thua = int(input('Nhập số muốn tính giai thừa: '))
    if giai_thua < 0:
        print(f'Không tính được giai thừa số: {giai_thua}\n')
        exit
    else:
        print(f'{giai_thua}! = {tinh_giai_thua(giai_thua)}\n')

# tính giai thừa
def tinh_giai_thua(n):
    tich = i = 1
    while i <= n:
        tich = tich * i
        i += 1

    return tich

"""Bài 6"""
def bai_6():
    so_ngto = int(input('Nhập số nguyên bạn muốn kiểm tra: '))
    if so_ngto <= 0:
        print(f'Số được kiểm tra phải lớn hơn 0 \n')
        exit
    else:
        so_nguyen_to(so_ngto)

# Kiểm tra số nguyên tố
def so_nguyen_to(n):
    result = []
    i = 2
    while i < n:
        if n % i == 0:
            result.append(i)
        i += 1

    if len(result) >= 1:
        print(f'Số bị chia = {result}')
        print(f'{n} không phải số nguyên tố\n')
    else:
        print(f'{n} là số nguyên tố\n')

"""Bài 7"""
def bai_7():
    num1 = input('Nhập số thứ nhất: ')
    num2 = input('Nhập số thứ hai: ')

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        if not num1.isdigit():
            print(f'Số {num1} không phải số nguyên')
        elif not num2.isdigit():
            print(f'{num2} không phải số nguyên')
        return

    calculation(num1, num2)

# Các phép tính cơ bản
def calculation(a, b):
    print('- Các phép tính cơ bản là:')
    print(f"Cộng: {a} + {b} = {a + b}")
    print(f"Trừ: {a} - {b} = {a - b}")
    print(f"Nhân: {a} * {b} = {a * b}")

    try:
        print(f"Chia: {a} / {b} = {a / b}\n")
    except ZeroDivisionError:
        print('Không chia được cho 0\n')

# Chạy chương trình
menu()
