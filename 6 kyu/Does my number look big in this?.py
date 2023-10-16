def narcissistic(value):
    num_digits = len(str(value))
    total = sum(int(digit) ** num_digits for digit in str(value))
    return total == value

print(narcissistic(7))

def narciss(value):
    new_digit = len(str(value))
    total = sum(int(digit) ** new_digit for digit in str(value))
    return total == value

print(narciss(7))
print(narciss(153))