def check_digit(number, index1, index2, digit):
    return str(digit) in str(number)[index1:index2+1] or str(digit) in str(number)[index2:index1+1]

print(check_digit(1234567, 1, 0, 1))