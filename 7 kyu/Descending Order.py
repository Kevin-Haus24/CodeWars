def descending_order(num):
    ans = [x for x in str(num)]
    ans = sorted(ans, reverse=True)
    return int(''.join(ans))

print(descending_order(123456789))