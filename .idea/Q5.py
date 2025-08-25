class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Lương: {self.salary}"


employees = []

while True:
    print("1. Thêm nhân viên")
    print("2. Xóa nhân viên")
    print("3. Tìm kiếm")
    print("4. Hiển thị tất cả")
    print("5. Thoát")

    choice = input("Chọn: ")

    if choice == '1':
        id = input("ID: ")
        name = input("Tên: ")
        salary = int(input("Lương: "))
        employees.append(Employee(id, name, salary))

    elif choice == '2':
        id_xoa = input("ID cần xóa: ")
        for i, emp in enumerate(employees):
            if emp.id == id_xoa:
                del employees[i]
                print("Đã xóa!")
                break

    elif choice == '3':
        keyword = input("Từ khóa: ")
        for emp in employees:
            if keyword in emp.name or keyword in emp.id:
                print(emp)

    elif choice == '4':
        for emp in employees:
            print(emp)

    elif choice == '5':
        break