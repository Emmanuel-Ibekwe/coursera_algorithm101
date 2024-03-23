# def optimal_summands(n):
#     summands = []
#     i = 1
#     sum_of_nums = 0
#     while sum_of_nums < n:
#         diff = n - (sum_of_nums + i)
#         if (diff in summands) or (diff == i):
#             i += 1
#             continue
#         else:
#             summands.append(i)
#             sum_of_nums = sum(summands)
#             i += 1

#     # write your code here
#     return summands


def optimal_summands(n):
    summands = []
    current = 1

    while n > 0:
        # if n <= 2 * current:
        if n - current <= current:
            summands.append(n)
            break
        else:
            summands.append(current)
            n -= current
            current += 1

    return summands


# print(optimal_summands(1000))
# print(optimal_summands(100))
# print(optimal_summands(8))


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
