from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


t = int(input())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    results.append(lcm(a, b))

print("\n".join(map(str, results)))
