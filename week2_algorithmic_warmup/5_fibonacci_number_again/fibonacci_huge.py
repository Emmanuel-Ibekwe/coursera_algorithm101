# def fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m

def pisana_period(m):
    a, b = 0, 1
    period = 0

    for _ in range(m * m):
        a, b = b, (a + b) % m
        if(a, b) == (0, 1):
            return period + 1
        period += 1

def fibonacci_huge(n, m):

    if n <= 1:
        return n

    period = pisana_period(m)
    n = n % period

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous +  current) % m
    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
