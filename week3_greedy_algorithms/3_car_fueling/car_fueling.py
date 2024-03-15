from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    current_stop = 0
    next_stop = 0
    remaining_mileage = tank
    total_distance = 0
    refills = 0
    n = len(stops)
    for i in range(n):
        current_stop = stops[i]
        if i < n - 1:
            next_stop = stops[i + 1]
        else: 
            next_stop = distance
        if i == 0: 
            remaining_mileage = remaining_mileage - stops[i]
            total_distance = stops[i]
            
        if total_distance + remaining_mileage < next_stop:
            refills += 1
            remaining_mileage = tank
        if total_distance + remaining_mileage < next_stop:
            return -1
  
        total_distance = next_stop
        remaining_mileage = (current_stop + remaining_mileage) - total_distance

    return refills
        

        


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
