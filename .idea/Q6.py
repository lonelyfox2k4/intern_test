def pangram_check(chuoi):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    str_lower = set(str.lower())
    return alphabet.issubset(str_lower)

# Test
str = input("Nhập chuỗi: ")
if pangram_check(str):
    print("Đây là pangram")
else:
    print("Đây không phải pangram")