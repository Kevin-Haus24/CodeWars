def encode(s):
    return ''.join(str(1 - ord(c) % 2) if c.isalpha() else c for c in s )
print(encode('Hello World!'))


def encode1(s):
    a = ''
    for c in s:
        if c.isalpha():
            a += str(1 - ord(c) % 2)
        else:
            a += c
    return a
print(encode1('Hello World!'))


def encode2(s):
    return s.lower().replace('a', '0').replace('b', '1').replace('c', '0').replace('d', '1').replace('e', '0').replace(
        'f', '1').replace('g', '0').replace('h', '1').replace('i', '0').replace('j', '1').replace('k', '0').replace('l',
                                                                                                                    '1').replace(
        'm', '0').replace('n', '1').replace('o', '0').replace('p', '1').replace('q', '0').replace('r', '1').replace('s',
                                                                                                                    '0').replace(
        't', '1').replace('u', '0').replace('v', '1').replace('w', '0').replace('x', '1').replace('y', '0').replace('z',
                                                                                                                    '1')
print(encode2('Hello World!'))

