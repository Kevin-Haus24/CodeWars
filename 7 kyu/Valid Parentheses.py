def valid_parentheses(paren_str):
    if paren_str == '':
        return True
    if paren_str[0] == ')' or paren_str[-1] == '(':
        return False
    open = 0
    close = 0
    for i in paren_str:
        if close > open: return False
        if i == '(': open += 1
        else: close += 1

    if paren_str.count('(') == paren_str.count(')'):
        print(paren_str[1:3])
        return True
    return False


print(valid_parentheses('())(()'))
