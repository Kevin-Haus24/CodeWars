def rgb(r, g, b):
    if r < 0: r = 0
    if g < 0: g = 0
    if b < 0: b = 0
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255

    red = hex(r)[2:].upper()
    green = hex(g)[2:].upper()
    blue = hex(b)[2:].upper()

    rgb1 = [red, green, blue]
    for i in range(len(rgb1)):
        if len(rgb1[i]) < 2:
            rgb1[i] = f'0{rgb1[i]}'

    return ''.join(rgb1)


print(rgb(0, 0, 0), "000000")
print(rgb(1, 2, 3), "010203")
print(rgb(255, 255, 255), "FFFFFF")
print(rgb(254, 253, 252), "FEFDFC")
print(rgb(-20, 275, 125), "00FF7D")
print(rgb(36 ,214 ,-181), '24D600')