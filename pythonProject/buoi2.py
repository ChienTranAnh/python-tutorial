# Menu chọn bài tập
def menu():
    while True:
        print()
        print('=== Chọn bài tập bạn muốn xem bằng cách nhập số đầu mục tương ứng ===')
        print('1. Mục 1 - Bài 1: In ra dãy số từ . . . đến . . . với bước số')
        print('2. Mục 2 - Bài 2: Dùng List Comprehension để tạo list số chẵn/lẻ')
        print('3. Mục 2 - Bài 3: Tạo Generator để sinh ra dãy số Fibonacci')
        print('4. Mục 3 - Bài 4: Đọc ghi file danh sách học viên của buổi 1')
        print('5. Mục 4 - Bài 5: Viết chương trình tải nội dung từ 1 trang web sử dụng request')
        print('87. Thoát')
        choice = int(input('Mời chọn: '))

        if choice == 1:
            bai_1()
        elif choice == 2:
            bai_2()
        elif choice == 3:
            bai_3()
        elif choice == 4:
            import quan_ly_hoc_vien
            quan_ly_hoc_vien.main()
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
        # dùng hàm lambda & hàm filter()
        result = list(filter(lambda y: y % 2 == 0, chuoi))
    elif typed == 'le':
        # dùng List Comprehension
        result = [j for j in chuoi if j % 2 != 0]

    i = 0
    while i < len(result)-1:
        print(result[i], end=', ')
        i += 1
    print(result[i])

"""Bài 2"""
def bai_2():
    bai_1()

# Chạy chương trình
menu()
