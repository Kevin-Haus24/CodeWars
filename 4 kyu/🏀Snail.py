def flatten_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    return flattened_list

def snail(snail_map):
    ans = []
    ans.append(snail_map[0][:-1])

    for i in range(len(snail_map)):
        ans.append(snail_map[i][-1])

    ans.append(snail_map[-1][:-1][::-1])

    ans.append(snail_map[1][0])

    ans.append(snail_map[1][1])

    return flatten_list(ans)

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))