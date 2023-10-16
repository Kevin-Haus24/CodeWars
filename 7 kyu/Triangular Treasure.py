def triangular(n):
    return n * (n+1) // 2


print(triangular(0), 0)
print(triangular(2), 3)
print(triangular(3), 6)
print(triangular(4), 10)
print(triangular(9), 45)
print(triangular(-10), 0)
print(triangular(90000000), 45)