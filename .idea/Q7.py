cau = input("Nhập một câu: ")
words = cau.lower().split()

dem_tu = {}
for word in words:
    # Loại bỏ dấu câu
    word = ''.join(char for char in word if char.isalnum())
    dem_tu[word] = dem_tu.get(word, 0) + 1

print("Số lần xuất hiện của từng từ:")
for word, count in dem_tu.items():
    print(f"'{word}': {count}")