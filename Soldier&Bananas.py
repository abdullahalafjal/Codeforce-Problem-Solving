def calculate_borrow(k, n, w):
    total_cost = k * (w * (w + 1)) // 2
    borrow = max(0, total_cost - n)
    return borrow


k, n, w = map(int, input().split())
print(calculate_borrow(k, n, w))
