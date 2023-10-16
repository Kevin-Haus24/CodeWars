def array_diff(a, b):
    for j in b:
        while j in a:
            index = a.index(j)
            a.pop(index)
    return a
print(array_diff([1, 1, 1, 1, 2, 2], [1]))