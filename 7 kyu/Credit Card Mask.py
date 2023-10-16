def maskify(cc):
    lft = cc[-4:]
    rgh = cc[:-4]
    for index, value in enumerate(rgh):
        rgh = rgh.replace(value, '#')
    return rgh + lft

print(maskify("4556364607935616"))