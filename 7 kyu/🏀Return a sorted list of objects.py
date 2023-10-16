def sort_list(sort_by, lst):

    list_a = sorted(lst.items(), key=lambda x: x[1])
    return list_a


print(sort_list("a",[{"a": 1, "b": 3}, {"a": 3, "b": 2}, {"a": 2, "b": 40}, {"a": 4, "b": 12}]))