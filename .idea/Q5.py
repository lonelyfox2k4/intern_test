def tong_chu_so(n):
    return sum(int(digit) for digit in str(abs(n)))

# Test
n = int(input("Nhập số nguyên: "))
print(f"Tổng các chữ số của {n}: {tong_chu_so(n)}")