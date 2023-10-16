import math
def triangle_type(a, b, c):
    a, b, c = sorted([a, b, c])
    if (a + b) > c:
        if a > 0 and a * a + b * b == c * c: return 2
        if a > 0 and a * a + b * b < c * c: return 3
        return 1
    return 0


print(triangle_type(7, 3, 2), 0)  # Not triangle
print(triangle_type(2, 4, 6), 0)  # Not triangle
print(triangle_type(8, 5, 7), 1)  # Acute
print(triangle_type(3, 4, 5), 2)  # Right
print(triangle_type(7, 12, 8), 3)  # Obtuse