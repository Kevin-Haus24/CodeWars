def solve(s):
    if s == '': return None
    alph = dict.fromkeys(s)
    a_key = [s.count(a) for a in alph]
    collage = {}
    for i, j in zip(alph, a_key):
        collage.update(dict.fromkeys(i, j))
    if len(collage) == 1: return True
    if sum(a_key) == len(a_key): return True
    if a_key.count(1) == 1 and (sum(a_key) - 1) % (len(a_key)-1) > 0: return False
    if a_key.count(1) == 1: return True
    if max(a_key) - min(a_key) > 1: return False
    if sum(a_key) % len(a_key) == 0: return False
    if a_key.count(1) > 1 and (max(a_key) > 2 or a_key.count(2) > 1): return False
    if max(a_key) - 1 == min(a_key): return True
    else: return True
    return keys


print(solve('abbccc'), '9')     #False)