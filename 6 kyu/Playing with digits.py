def dig_pow(n, p):
    num = [int(x) for x in str(n)]
    ans = 0
    for i in num:
        ans += i ** p
        p += 1
    if ans % n == 0: return ans // n
    return -1

print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)
print(dig_pow(41, 5), 25)
print(dig_pow(114, 3), 9)
print(dig_pow(8, 3), 64)
print(dig_pow(46288, 5), -1)