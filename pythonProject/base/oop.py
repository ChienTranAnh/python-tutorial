class Student:
    # Hàm khởi tạo (constructor) với các thuộc tính name và age
    def __init__(self, name, age):
        self.name = name  # Thuộc tính tên
        self.age = age    # Thuộc tính tuổi
    
    # Phương thức hiển thị thông tin học viên
    def hien_thi_thong_tin(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}")

# Ví dụ sử dụng lớp Student
student1 = Student("Nguyễn Văn A", 16)
student2 = Student("Trần Thị B", 17)

# Hiển thị thông tin của các học viên
student1.hien_thi_thong_tin()
student2.hien_thi_thong_tin()


# Lớp Person (lớp cơ sở)
class Person:
    def __init__(self, name, age):
        self.name = name  # Thuộc tính tên
        self.age = age  # Thuộc tính tuổi

    def hien_thi_thong_tin(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}")

# Lớp Student kế thừa từ lớp Person
class Student(Person):
    def __init__(self, name, age, lop):
        super().__init__(name, age)  # Gọi hàm khởi tạo của lớp Person
        self.lop = lop  # Thuộc tính lớp (class)

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()  # Gọi phương thức hiển thị từ lớp Person
        print(f"Lớp: {self.lop}")  # Thêm thông tin lớp

# Lớp Teacher kế thừa từ lớp Person
class Teacher(Person):
    def __init__(self, name, age, mon_hoc):
        super().__init__(name, age)  # Gọi hàm khởi tạo của lớp Person
        self.mon_hoc = mon_hoc  # Thuộc tính môn học (subject)

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()  # Gọi phương thức hiển thị từ lớp Person
        print(f"Môn dạy: {self.mon_hoc}")  # Thêm thông tin môn học

# Tạo đối tượng Student
student = Student("Nguyễn Văn A", 16, "10A")
# Tạo đối tượng Teacher
teacher = Teacher("Trần Thị B", 35, "Toán")

# Hiển thị thông tin của học viên và giáo viên
print("\nThông tin học viên:")
student.hien_thi_thong_tin()

print("\nThông tin giáo viên:")
teacher.hien_thi_thong_tin()
