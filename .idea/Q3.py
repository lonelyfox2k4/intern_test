danh_sach = []
print("Nhập các số nguyên (nhập 'done' để kết thúc):")
while True:
    inp = input("Nhập số: ")
    if inp.lower() == 'done':
        break
    danh_sach.append(int(inp))

# Lọc số chia hết cho 2 và 3
ket_qua = [so for so in danh_sach if so % 2 == 0 and so % 3 == 0]
print("Các số chia hết cho 2 và 3:", ket_qua)