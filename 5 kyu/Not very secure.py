import re
def alphanumeric(password):
    if re.search(r'[ !""#$%&''()*+,-./:;<=>?@[\]^_`]', password): return False
    return len(re.split('[1234567890]', password)) > 1 and not(re.search(r'[_ ()!?><{}`*]', password))

print(alphanumeric("hello world_"), False)
print(alphanumeric("PassW0rd"), True)
print(alphanumeric("1qBfs>XSBCwB1WKjiL5hVXf"), False)