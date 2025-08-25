danh_sach = []
print("Nhập các số nguyên (nhập số âm để kết thúc):")
while True:
    so = int(input("Nhập số: "))
    if so < 0:
        break
    danh_sach.append(so)

so_chan = [so for so in danh_sach if so % 2 == 0]
print("Danh sách số chẵn:", so_chan)