def is_nearly_lucky(n):
    lucky_digits = sum(1 for digit in str(n) if digit in "47")

    if all(digit in "47" for digit in str(lucky_digits)):
        return "YES"
    else:
        return "NO"


n = int(input())
print(is_nearly_lucky(n))
