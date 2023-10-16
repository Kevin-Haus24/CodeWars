def move_zeros(lst):
    count = lst.count(0)
    lst = [x for x in lst if x != 0]
    for i in range(count):
        lst.append(0)
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))