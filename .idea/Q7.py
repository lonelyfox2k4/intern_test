class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Giá: {self.price}"


products = []

while True:
    print("1. Thêm sản phẩm")
    print("2. Hiển thị danh sách")
    print("3. Tìm theo tên")
    print("4. Xóa theo ID")
    print("5. Thoát")

    choice = input("Chọn: ")

    if choice == '1':
        id = input("ID: ")
        name = input("Tên: ")
        price = float(input("Giá: "))
        products.append(Product(id, name, price))

    elif choice == '2':
        for p in products:
            print(p)

    elif choice == '3':
        ten = input("Tên cần tìm: ")
        for p in products:
            if ten.lower() in p.name.lower():
                print(p)

    elif choice == '4':
        id_xoa = input("ID cần xóa: ")
        for i, p in enumerate(products):
            if p.id == id_xoa:
                del products[i]
                break

    elif choice == '5':
        break