from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


from functools import cmp_to_key

def largest_concatenate(integers):
    # Custom comparator function to compare two integers when concatenated
    def compare(a, b):
        ab = int(str(a) + str(b))
        ba = int(str(b) + str(a))
        return ba - ab  # Compare in descending order

    # Sort integers using the custom comparator
    sorted_integers = sorted(integers, key=cmp_to_key(compare))

    # Concatenate sorted integers to form the largest number
    largest_number = ''.join(map(str, sorted_integers))

    return largest_number

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_concatenate(input_numbers))
