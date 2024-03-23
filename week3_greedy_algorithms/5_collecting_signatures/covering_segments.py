from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments.sort(key=lambda x: x[1])  # Sort segments by their right endpoint
    points = []
    i = 0
    while i < len(segments):
        rightmost = segments[i][1]
        points.append(rightmost)
        # Skip segments that are already covered by this point
        while i < len(segments) and segments[i][0] <= rightmost:
            i += 1
            # write your code here
            # for s in segments:
            #     points.append(s.start)
            #     points.append(s.end)

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments = list(map(lambda x: x, zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

# 4 7
# 1 3
# 2 5
# 5 6
