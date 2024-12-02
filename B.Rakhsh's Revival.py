def minimum_timars(t, test_cases):
    results = []
    for n, m, k, s in test_cases:
        operations = 0
        current_zeros = 0

        for char in s:
            if char == "0":
                current_zeros += 1
            else:

                if current_zeros >= m:
                    operations += (current_zeros + k - 1) // k
                current_zeros = 0

        if current_zeros >= m:
            operations += (current_zeros + k - 1) // k

        results.append(operations)

    return results


t = int(input())
test_cases = []
for _ in range(t):
    n, m, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, m, k, s))

results = minimum_timars(t, test_cases)
print("\n".join(map(str, results)))
