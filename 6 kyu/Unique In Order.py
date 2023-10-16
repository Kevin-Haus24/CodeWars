def unique_in_order(sequence):
    if not(sequence): return []
    ans = [sequence[0]]
    for i in range(1, len(sequence)):
        if ans[-1] != sequence[i]: ans.append(sequence[i])
        else: pass
    return ans


print(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
print(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])
print(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])
print(unique_in_order("AA"), ["A"])
print(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
