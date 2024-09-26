import sys

# Menu lựa chọn
def menu():
    while True:
        print()
        print("=== Quản lý danh sách học viên ===")
        print("1. Thêm học viên")
        print("2. Hiển thị danh sách học viên")
        print("3. Sửa thông tin học viên")
        print("4. Xóa học viên")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            them_hoc_vien()
        elif choice == '2':
            hien_thi_danh_sach()
        elif choice == '3':
            sua_thong_tin_hoc_vien()
        elif choice == '4':
            xoa_hoc_vien()
        elif choice == '5':
            sys.exit('Thoát!')
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

# Hiển thị danh sách học viên
def hien_thi_danh_sach():
    hoc_vien = doc_file()
    if hoc_vien == False:
        print("Danh sách học viên trống.\n")
        return

    # In danh sách học viên
    print("\nDanh sách học viên:")
    for idx, hs in enumerate(hoc_vien):
        print(f"{idx + 1}. Tên: {hs['ten']}, Tuổi: {hs['tuoi']}, Lớp: {hs['lop']}")

# Thêm học viên vào danh sách
def them_hoc_vien():
    ten = input("Nhập tên học viên: ")
    tuoi = input("Nhập tuổi: ")
    lop = input("Nhập lớp: ")

    # Tạo học viên dưới dạng Dictionary
    hoc_vien = {
        'ten': ten,
        'tuoi': tuoi,
        'lop': lop
    }

    # Thêm học viên vào danh sách
    hoc_vien_file = open("hoc_vien.txt", "a")
    check = hoc_vien_file.write(f'{hoc_vien}')

    if check > 0:
        print(f"Đã thêm học viên \'{ten}\' vào danh sách.\n")
    else:
        print(f"Có lỗi, không thêm được học viên \'{ten}\' vào danh sách.\n")

    hoc_vien_file.close()

# Chỉnh sửa thông tin học viên
def sua_thong_tin_hoc_vien():
    hien_thi_danh_sach()

    try:
        index = int(input("Nhập số thứ tự của học viên cần sửa: ")) - 1
        if 0 <= index < len(danh_sach_hoc_vien):
            hoc_vien = danh_sach_hoc_vien[index]
            print(f"Sửa thông tin cho học viên {hoc_vien['ten']}")
            
            hoc_vien['ten'] = input("Nhập tên mới: ")
            hoc_vien['tuoi'] = input("Nhập tuổi mới: ")
            hoc_vien['lop'] = input("Nhập lớp mới: ")
            print("Thông tin đã được cập nhật.\n")
        else:
            print("Không có học viên nào với số thứ tự này.\n")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.\n")

# Xóa học viên
def xoa_hoc_vien():
    hien_thi_danh_sach()
    
    try:
        index = int(input("Nhập số thứ tự của học viên cần xóa: ")) - 1
        if 0 <= index < len(danh_sach_hoc_vien):
            hoc_vien = danh_sach_hoc_vien.pop(index)
            print(f"Đã xóa học viên {hoc_vien['ten']} khỏi danh sách.\n")
        else:
            print("Không có học viên nào với số thứ tự này.\n")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.\n")

def doc_file(mode = 'rt'):
    with open('hoc_vien.txt', mode, encoding='utf-8') as my_file:
        contents = my_file.read().strip()

    if not contents:
        hoc_vien = False
    else:
        # Thêm dấu phẩy để  thành danh sách JSON
        hoc_vien = contents.replace('}{', '},{')

        # Đổi dấu ' thành "
        data = f"[{hoc_vien}]"
        data = data.replace('\'', '\"')

        # Chuyển chuỗi thành danh sách các dictionary
        import json
        hoc_vien = json.loads(data)

    return hoc_vien

# Chạy chương trình
menu()
