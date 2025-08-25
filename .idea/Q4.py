cau = input("Nhập một câu: ")
words = cau.split()
dao_nguoc = " ".join(reversed(words))
print("Câu đảo ngược:", dao_nguoc)