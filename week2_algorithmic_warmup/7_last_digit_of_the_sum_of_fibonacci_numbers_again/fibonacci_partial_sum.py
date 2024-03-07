# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def fibonacci_partial_sum_optimized(from_, to):
    # Define the Pisano period for modulo 10
    pisano_period = 60

    # Adjust the 'from_' and 'to' indices to fit into the Pisano period
    from_ %= pisano_period
    to %= pisano_period

    # Handle the case where 'to' is smaller than 'from_'
    if to < from_:
        to += pisano_period

    # Initialize variables
    current, next_ = 0, 1
    partial_sum = 0

    # Calculate the partial sum of Fibonacci numbers modulo 10
    for i in range(to + 1):
        if i >= from_:
            partial_sum = (partial_sum + current) % 10

        current, next_ = next_, (current + next_) % 10

    return partial_sum

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_optimized(from_, to))
