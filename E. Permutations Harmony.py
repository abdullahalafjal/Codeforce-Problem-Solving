def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if k > n:
            print("NO")
        else:
            print("YES")
            base_permutation = list(range(1, n + 1))

            for i in range(k):
                permutation = base_permutation[i:] + base_permutation[:i]
                print(" ".join(map(str, permutation)))


solve()
