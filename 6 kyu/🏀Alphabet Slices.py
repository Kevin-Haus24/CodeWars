import string
def solution(s):
    alph = string.ascii_lowercase
    rev_alph = string.ascii_lowercase[::-1]
    ans = ''
    val = []
    ind = []
    # for index, value in enumerate(s):
    #     if v
    return val, ind

print(solution('xabc'),        'xcba')
print(solution('abcxdef'),     'cbaxfed')
print(solution('abcxyz'),      'cbazyx')
print(solution('zahimzmstaz'), 'zaihmzmtsaz')
print(solution('jjjjjjjjklmnopqrstuv'), 'jjjjjjjvutsrqponmlkj')
print(solution('zyx'),         'zyx')
print(solution('ppqqrr'),      'pqprqr')
print(solution('gjaababbboo'), 'gjabababboo')