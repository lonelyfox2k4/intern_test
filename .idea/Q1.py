n = int(input("Nhập số phần tử n: "))

if n <= 0:
    fib = []
elif n == 1:
    fib = [0]
elif n == 2:
    fib = [0, 1]
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

print(f"Dãy Fibonacci {n} phần tử:", fib)