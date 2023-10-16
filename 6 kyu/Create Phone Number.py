def create_phone_number(n):
    n = [str(x) for x in n]
    n = ''.join(n)
    return f'({n[0:3]}) {n[3:6]}-{n[6:10]}'
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))