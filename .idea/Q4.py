student_list = []
print("Nhập họ tên sinh viên (nhập 'done' để kết thúc)::")
while True:
    name = input("Nhập họ tên sinh viên: ")
    if name.lower() == 'done':
        break
    student_list.append(name)

#sort by students' name
student_list.sort()
print("Tên sinh viên đã sắp xếp: ")
for i, ten in enumerate(student_list, 1):
    print(f"{i}. {ten}")