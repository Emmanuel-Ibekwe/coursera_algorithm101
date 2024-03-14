from sys import stdin

def insertion_sort_desc(arr, weights, values):
    for i in range(1, len(arr)):
        key = arr[i]
        w_key = weights[i]
        v_key = values[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            weights[j + 1] = weights[j]
            values[j + 1] = values[j]
            j -= 1
        arr[j + 1] = key
        weights[j + 1] = w_key
        values[j + 1] = v_key

def sorted_unit_values(values, weights):
    unit_values = []
    for i in range(len(values)):
        unit_value = values[i]/weights[i]
        unit_values.append(unit_value)
    insertion_sort_desc(unit_values, weights, values)

        

def optimal_value(capacity, weights, values):
    sorted_unit_values(values, weights)
    # value = 0.
    total_value = 0
    for i in range(len(values)):
        if capacity == 0:
            return total_value
        amt = min(weights[i], capacity)
        total_value = total_value + amt * (values[i]/weights[i])
        weights[i] = weights[i] - amt
        capacity -= amt
    
    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))



