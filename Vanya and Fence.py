def minimum_road_width(n, h, heights):
    total_width = 0

    for i in heights:
        if i > h:
            total_width += 2
        else:
            total_width += 1

    return total_width


n, h = map(int, input().split())
heights = list(map(int, input().split()))
print(minimum_road_width(n, h, heights))
