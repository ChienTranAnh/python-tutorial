# Khởi tạo danh sách học viên (List các học viên là Dictionary)
danh_sach_hoc_vien = []

# Menu lựa chọn
def menu():
    while True:
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
            import baitap
            baitap.main()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

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
    danh_sach_hoc_vien.append(hoc_vien)
    print(f"Đã thêm học viên {ten} vào danh sách.\n")

# Hiển thị danh sách học viên
def hien_thi_danh_sach():
    if not danh_sach_hoc_vien:
        print("Danh sách học viên trống.\n")
        return False
    
    print("Danh sách học viên:")
    for idx, hs in enumerate(danh_sach_hoc_vien):
        print(f"{idx + 1}. Tên: {hs['ten']}, Tuổi: {hs['tuoi']}, Lớp: {hs['lop']}")
    print()

# Chỉnh sửa thông tin học viên
def sua_thong_tin_hoc_vien():
    if not hien_thi_danh_sach():
        return
    else:
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
    if not hien_thi_danh_sach():
        return
    else:
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

# Chạy chương trình
menu()
