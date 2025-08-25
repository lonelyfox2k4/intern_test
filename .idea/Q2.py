chuoi = input("Nhập chuỗi: ")
chuoi_sach = ''.join(char.lower() for char in chuoi if char.isalnum())

if chuoi_sach == chuoi_sach[::-1]:
    print("Chuỗi đối xứng")
else:
    print("Chuỗi không đối xứng")