def second_symbol(s, symbol):
    if (symbol not in s) or (s.count(symbol) == 1):
        return -1
    else:
        index = s.find(symbol)
        n_index = s.find(symbol, index + 1)
        return n_index

print(second_symbol('Hello world!!!','l'))