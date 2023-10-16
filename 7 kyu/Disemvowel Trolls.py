def disemvowel(string_): return ''.join([a for a in string_ if a.lower() not in 'aeiou'])

print(disemvowel('This website is for losers LOL'))