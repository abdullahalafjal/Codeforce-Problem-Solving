def minimum_capacity(n, stops):
    current_p = 0
    max_p = 0

    for a, b in stops:
        current_p = current_p - a + b
        max_p = max(max_p, current_p)

    return max_p


n = int(input())
stops = [tuple(map(int, input().split())) for _ in range(n)]
print(minimum_capacity(n, stops))
