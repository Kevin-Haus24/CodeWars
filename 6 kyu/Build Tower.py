def tower_builder(n_floors):

    na = [x for x in range(1, 1000, 2)]
    ns = [na[x] for x in range(n_floors)]

    ans = []

    for i in range(n_floors):
        qwa = '*' * ns[i]
        ans.append(qwa.center(ns[-1]))

    return ans


print(tower_builder(1), ['*'])
print(tower_builder(2), [' * ', '***'])
print(tower_builder(3), ['  *  ', ' *** ', '*****'])
print(tower_builder(4), ['   *   ', '  ***  ', ' ***** ', '*******'])