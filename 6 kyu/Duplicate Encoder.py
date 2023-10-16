def duplicate_encode(word):
    word = word.lower()
    ans = ''
    for i in word:
        if word.count(i) > 1: ans += ')'
        else: ans += '('
    return ans

print(duplicate_encode("din"), "(((")
print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("Success"), ")())())", "should ignore case")
print(duplicate_encode("(( @"), "))((")