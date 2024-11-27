def is_translation_correct(s, t):
    reversed_s = s[::-1]

    if reversed_s == t:
        return "YES"
    else:
        return "NO"


s = input().strip()
t = input().strip()
print(is_translation_correct(s, t))
