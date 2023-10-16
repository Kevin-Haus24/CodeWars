def find_outlier(integers):
    odd = [str(x) for x in integers if x % 2 != 0]
    even = [str(x) for x in integers if x % 2 == 0]
    if len(odd) > len(even): return int(''.join(even))
    else: return int(''.join(odd))

print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)