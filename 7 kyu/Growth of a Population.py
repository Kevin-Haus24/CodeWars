from math import *
def nb_year(p0, percent, aug, p):
    k = 0
    while p0 < p:
        p0 = floor(p0 + p0 * percent/100 + aug)
        k += 1
    return k



print(nb_year(1000, 2, 50, 1200), 3)
print(nb_year(1500, 5, 100, 5000), 15)
print(nb_year(1500000, 2.5, 10000, 2000000), 10)
print(nb_year(1500000, 0.25, 1000, 2000000), 94)
print()
print(nb_year(1000, 2, 50, 1214), 4)
#1000 2.0 50 1214
