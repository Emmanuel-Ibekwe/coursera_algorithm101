def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False


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

def lcm_efficient(a, b):
    return (a * b) // gcd_efficient(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_efficient(a, b))
