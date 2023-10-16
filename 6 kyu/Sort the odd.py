def sort_array(source_array):
    odd = sorted([x for x in source_array if x % 2 != 0])
    ind = 0
    for i in range(len(source_array)):
        if source_array[i] in odd:
            source_array[i] = odd[ind]
            ind += 1
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]), [])