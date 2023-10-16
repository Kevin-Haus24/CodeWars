def trim(phrase, size):
    if len(phrase) == size or len(phrase) < size: return phrase
    elif size - 3 > len(phrase):    return phrase
    elif len(phrase) <= 3 or size <= 3:   return f'{phrase[:size]}...'
    else: return f'{phrase[:size-3]}...'

print(trim("Creating kata is fun", 14))