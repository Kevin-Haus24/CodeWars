from collections import Counter
def find_uniq(arr):
    ans = Counter(arr).keys()
    a = [x for x in ans]
    return a[0] if arr.count(a[0]) == 1 else a[1]




print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
print(find_uniq([10, 10, 10, 1, 10]), 1)