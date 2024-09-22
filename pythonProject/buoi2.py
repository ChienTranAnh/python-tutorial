# Menu chọn bài tập
def menu():
    while True:
        print('=== Chọn bài tập bạn muốn xem bằng cách nhập số đầu mục tương ứng ===')
        print('1. Mục 1 - Bài 1: In ra dãy số từ . . . đến . . . với bước số')
        print('2. Mục 2 - Bài 2: Tính tổng của các số chẵn/lẻ')
        print('3. Mục 2 - Bài 3: Kiểm tra chuỗi Palindrome')
        print('4. Mục 3 - Bài 4: Đếm số từ trong một câu được nhập')
        print('5. Mục 4 - Bài 5: Tính giai thừa')
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
    typed = input('Bạn muốn in các số chẵn hay lẻ. Nhập chữ "chan" hoặc "le": ')
    chuoi = []

    for i in range(start_num, number+1):
        chuoi.append(i)

    if typed == 'chan':
        result = list(filter(lambda y: y % 2 == 0, chuoi))
    elif typed == 'le':
        result = list(filter(lambda y: y % 2 != 0, chuoi))

    i = 0
    while i < len(result)-1:
        print(result[i], end=', ')
        i += 1
    print(result[i])

# Chạy chương trình
menu()
