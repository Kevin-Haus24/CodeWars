def shortener(message):
    if len(message) <= 160 or message.count(' ') == 0: return message
    s1 = message.count(' ')
    while len(message) > 160 and s1 > 0:
        i = message.rindex(' ')
        message = message[:i] + '' + message[i+1].upper() + message[i+2:]
        s1 -= 1
    return message
print(shortener('SMS messages are limited to 160 characters. It tends to be irritating, '
               'especially when freshly written message is 164 characters long. '
               'SMS messages are limited to 160 characters. It tends to be irritating, '
               'especially when freshly written message is 164 characters long.'))