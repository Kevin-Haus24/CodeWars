def barbell_weight(barbell):
    bar = 20
    weight = {'R':25, 'B':20, 'Y':15, 'G':10, 'W':5,
              'r':2.5, 'b':2, 'y':1.5, 'g':1, 'w':0.5, 'c':2.5}
    barbell = barbell.replace('-', '')
    for i in barbell:
        bar += weight[i]
    return bar


print(barbell_weight("---------wc------------------cw---------"))