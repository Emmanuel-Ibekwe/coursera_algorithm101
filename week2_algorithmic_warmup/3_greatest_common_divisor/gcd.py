def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_efficient(a, b):
    if a > b:
        a1 = a
        b1 = b
    else:
        a1 = b
        b1 = a

    if b1 == 0:
        return a
    c = a1 % b1
    return gcd_efficient(b1, c)


# print(gcd_efficient(3918848, 1653264))
# print(gcd_efficient(1653264, 3918848))

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_efficient(a, b))
