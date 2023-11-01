def decrypt(encrypted_text, n):
    if not(encrypted_text) or n < 1: return encrypted_text
    for _ in range(n):
        ans = ''
        s1, s2 = encrypted_text[:len(encrypted_text) // 2], encrypted_text[len(encrypted_text) // 2:]
        for i in range(len(encrypted_text)):
            try:
                ans += s2[i]
                ans += s1[i]
            except IndexError: pass
        encrypted_text = ans

    return encrypted_text


def encrypt(text, n):
    if not(text) or n < 1: return text
    for _ in range(n):
        i1, i2 = '', ''
        for i, v in enumerate(text):
            if i % 2 != 0: i1 += v
            else: i2 += v
        text = i1 + i2
    return text


print(encrypt('Привет меня зовут Марк', 5))
print(decrypt('е взкмти р уряатвПнМео', 5))