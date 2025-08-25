import random

# Sinh 100 số ngẫu nhiên
so_ngau_nhien = [random.randint(1, 1000) for _ in range(100)]

# Lọc các bội của 7, loại bỏ trùng
boi_cua_7 = list(set([so for so in so_ngau_nhien if so % 7 == 0]))
boi_cua_7.sort()

print("100 số ngẫu nhiên:", so_ngau_nhien)
print("Các số là bội của 7 (không trùng):", boi_cua_7)