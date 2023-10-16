import math
def is_square(n):
    try:
        a = int(math.sqrt(n))
        return math.sqrt(n) == int(math.sqrt(n))
    except:
        return False

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))