def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        arr = [0] * (n + 1)
        arr[0] = 0
        arr[1] = 1
        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

# print(fibonacci(100))


for i in range(20):
    print(fibonacci(i))
