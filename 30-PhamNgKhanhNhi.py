# Danh sách để lưu thông tin các sinh viên.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ---")

    # Gọi thử hàm add_student để kiểm tra
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    print("\nDanh sách sinh viên hiện có:")
    for sv in student_list:
        print(f"- {sv['name']} ({sv['year_of_birth']}, {sv['address']})")
        
 feature/print-list
def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên
      theo định dạng:
      " - Ten: [Họ tên], Nam sinh: [Năm sinh], Dia chi: [Địa chỉ]"
    """
    print("--- DANH SACH SINH VIEN ---")
    if len(student_list) == 0:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
print_student_list()

def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên
      theo định dạng:
      " - Ten: [Họ tên], Nam sinh: [Năm sinh], Dia chi: [Địa chỉ]"
    """
    print("--- DANH SACH SINH VIEN ---")
    if len(student_list) == 0:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")
print_student_list()

print("Hoàn thiện chức năng in danh sách sinh viên")

def search_student(name):
    """
    YÊU CẦU 3: Hoàn thiện hàm này.
    - Nhận vào tên sinh viên cần tìm.
    - Tìm trong danh sách student_list.
    - Nếu tìm thấy thì in ra thông tin sinh viên.
    - Nếu không tìm thấy thì in "Không tìm thấy sinh viên".
    """
    found = False
    for sv in student_list:
        if sv['name'].lower() == name.lower():
            print(f"Tìm thấy: {sv['name']} - {sv['year_of_birth']} - {sv['address']}")
            found = True
    if not found:
        print("❌ Không tìm thấy sinh viên nào có tên đó.")
if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ---")

    # Danh sách mẫu
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    print("\nTÌM KIẾM SINH VIÊN:")
    search_student("Tran Thi Binh")
    search_student("Nguyen Thi Mai")  

