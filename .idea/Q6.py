class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


# Thư viện sách
library = []


# Thêm sách
def them_sach():
    title = input("Tên sách: ")
    author = input("Tác giả: ")
    year = int(input("Năm: "))
    library.append(Book(title, author, year))


# Tìm sách
def tim_sach():
    keyword = input("Nhập từ khóa: ")
    for book in library:
        if keyword.lower() in book.title.lower():
            print(book)


# Menu
while True:
    print("1. Thêm sách")
    print("2. Hiển thị tất cả")
    print("3. Tìm sách")
    print("4. Thoát")

    choice = input("Chọn: ")

    if choice == '1':
        them_sach()
    elif choice == '2':
        for book in library:
            print(book)
    elif choice == '3':
        tim_sach()
    elif choice == '4':
        break