import string
def alphabet_position(text):
    alph = string.ascii_uppercase
    text = text.upper()
    text = ' '.join(x for x in text if x in alph)
    for index, value in enumerate(alph, 1):
        text = text.replace(value, str(index))
    return text

print(alphabet_position("The sunset sets at twelve o' clock."))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
