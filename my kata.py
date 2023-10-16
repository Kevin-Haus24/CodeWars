from solution import max_len_with_condition
import codewars_test as test
import random
import string

def generate_random_string(fl=True, digit=True, space=False, length=100, uppercase=True, special_chars=True):
    chars = ''
    if uppercase: chars += string.ascii_uppercase
    if special_chars: chars += ' '
    if digit: chars += string.digits
    if space:
        chars = ' '
        length = 1
    return ''.join(random.choice(chars) for _ in range(length))

def max_len_with_condition1(s):
    s = s.replace('O', 'N').replace('P', 'N').replace(' ', '')
    if len(s) == 0: return 0
    if s == ' ': return 0
    if s.isalpha() == False: return -1
    while 'NN' in s:
        s = s. replace('NN', 'N N')
    ans = max(len(c) for c in s.split())
    return ans

@test.describe("max_len")
def tests():
    @test.it("should return the maximum length")
    def test_max_len():
        for _ in range(500):
            dig_false, dig_true = [False] * 10, [True]
            sp_false, sp_true = [False] * 100, [True]
            digitiss, sp = dig_true + dig_false, sp_false + sp_true
            digitiss, sp = random.choice(digitiss), random.choice(sp)
            random_string = generate_random_string(True, digitiss, sp)
            test.assert_equals(max_len_with_condition(random_string), max_len_with_condition1(random_string))
        test.assert_equals(max_len_with_condition('NOPNOPNOPNOPNOPONPON PONPONPOOOPNNOONNONNPNPONPNPONPPPONPO'), 1)


from solution import max_len_with_condition
import codewars_test as test


@test.describe("max_len")
def tests():
    @test.it("should return the maximum length")
    def answer():
        test.assert_equals(max_len_with_condition('AAANAPOAA'), 6)
        test.assert_equals(max_len_with_condition('NOPN OPNO'), 1)
        test.assert_equals(max_len_with_condition('NOPNOPN0P'), -1)
        test.assert_equals(max_len_with_condition(''), 0)
        test.assert_equals(max_len_with_condition('      NOP'), 1)
