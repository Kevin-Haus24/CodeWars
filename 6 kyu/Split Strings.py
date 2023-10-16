def solution(s):
    if len(s) % 2 != 0: s += '_'
    ans = []
    for i in range(0, len(s), 2):
        ans.append(s[i:i+2])
    return ans

print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution(""), [])
print(solution("x"), ["x_"])