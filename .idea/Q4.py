def co_chua_so(chuoi):
    return any(char.isdigit() for char in chuoi)

# Test
chuoi = input("Nhập chuỗi: ")
if co_chua_so(chuoi):
    print("Chuỗi có chứa số")
else:
    print("Chuỗi không chứa số")