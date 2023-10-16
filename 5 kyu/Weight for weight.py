def order_weight(strng):
    strng = strng.split()
    data = []
    for i in strng:
        ans = 0
        for j in i:
            ans += int(j)
        data.append(f'{str(i)}: {int(ans)}')
        data = sorted(data)
    return data

print(order_weight("103 123 4444 99 2000"))