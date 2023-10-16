def digital_root(n):
    n = str(n)
    ans = 0
    while len(n) > 1:
        for i in n:
            ans += int(i)
        if len(str(ans)) == 1:
            return ans
        else:
            n = str(ans)
            ans = 0
    return int(n)

print(digital_root(0))