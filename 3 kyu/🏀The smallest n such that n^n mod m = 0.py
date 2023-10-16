
def f(m:int) -> int:
    mini = 10**24
    for x in range(2, 100):
        q = m / x
        if q == int(q):
            q = int(q)
            if q**q % m == 0:
                mini = min(mini, q)
    return mini

print(f(13), 13)
print(f(27), 6)
print(f(420), 210)
print(f(666), 222)
print(f(1234567890), 411522630)