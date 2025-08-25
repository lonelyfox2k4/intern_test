def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
n = int(input("Nhập số n: "))
if kiem_tra_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải số nguyên tố")