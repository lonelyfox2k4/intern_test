try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = content.replace("Python", "Java")

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(new_content)

    print("Đã xử lý file thành công!")

except FileNotFoundError:
    print("Không tìm thấy file input.txt")