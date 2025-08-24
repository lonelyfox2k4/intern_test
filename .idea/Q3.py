def analyst_number(nums):
    largest = max(nums)
    lowest = min(nums)
    average = sum(nums) / len(nums)
    return largest, lowest, average


arr = list(map(int,input("Nhập vào một chuỗi các số ").split()))
largest, lowest, average = analyst_number(arr)
print("Số lớn nhất là: ",largest)
print("Số nhỏ nhất là: ",lowest)
print("Trung bình cộng: ",average)