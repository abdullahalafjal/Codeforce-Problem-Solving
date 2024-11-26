def decrease_number(n, k):
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
    return n


n, k = map(int, input().split())
print(decrease_number(n, k))
