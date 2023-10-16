def is_isogram(string):
    count = []
    string = string.lower()
    if string == '': return True
    for i in string:
        count.append(string.count(i))
    if sum(count) % len(string) == 0: return True
    else: return False

print(is_isogram("Dermatoglyphics"), True )
print(is_isogram("isogram"), True )
print(is_isogram("aba"), False)
print(is_isogram("moOse"), False)
print(is_isogram("isIsogram"), False)
print(is_isogram(""), True)