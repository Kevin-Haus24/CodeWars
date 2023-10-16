def two_are_positive(a, b, c):
    num = [a, b, c]
    ans = [x for x in num if x > 0]
    if len(ans) == 2: return True
    else: return False

print(two_are_positive(2, 4, -3), True)
print(two_are_positive(-4, 6, 8), True)
print(two_are_positive(4, -6, 9), True)
print(two_are_positive(-4, 6, 0), False)
print(two_are_positive(4, 6, 10), False)
print(two_are_positive(-14, -3, -4), False)