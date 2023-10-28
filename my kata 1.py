def flatten_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    return flattened_list

# Как в питоне [[1, 2], 3, 6, 9, [8, 7], 4, 5] превратить в [1,2,3,6,9,8,7,4,5]

def sum_mul(n, m):
    ans = []
    if n == 0 and m == 0: return 'INVALID'
    if m < 0: return 'INVALID'
    for i in range(m):
        if i % n == 0:
            ans.append(i)
    return sum(ans)

print(sum_mul(2, 9))











def to_jaden_case(string): return string.title()


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
print("How Can Mirrors Be Real If Our Eyes Aren't Real")