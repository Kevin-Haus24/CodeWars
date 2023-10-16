import math
def persistence(n):
    digit = [int(x) for x in str(n)]
    count = 0
    while len(digit) > 1:
        digit = [int(x) for x in str(math.prod(digit))]
        count += 1
    return count

print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)