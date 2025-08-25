def alphabet_count(str):
    count = {}
    for char in str.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    return char

# Test
str = input("Nhập chuỗi: ")
result = alphabet_count(str)
print(result)