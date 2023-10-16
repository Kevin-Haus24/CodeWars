def accum(s):
    s = [x for x in s]
    ans = ''
    for index, value in enumerate(s):
        ans = ans + value.upper() + value.lower() * index + '-'
    return ans[:-1]

print(accum("ZpglnRxqenU"))