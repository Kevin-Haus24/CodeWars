# import itertools
# def list_position(word):
#     alphabet = sorted(word)
#     ar = itertools.permutations(alphabet)
#     arl = set()
#     for e in ar:
#         arl.add(e)
#         if ''.join(e) == word:
#             return len(arl)

from math import factorial
from collections import Counter


def list_position(word):
    rank = 1
    n = len(word)

    for i, char in enumerate(word):
        smaller_chars = 0
        repeating_chars = Counter(word[i:])

        for c in repeating_chars:
            if c < char:
                smaller_chars += repeating_chars[c]

        total_permutations = factorial(n - i - 1)
        duplicate_permutations = 1

        for count in repeating_chars.values():
            duplicate_permutations *= factorial(count)

        rank += smaller_chars * total_permutations // duplicate_permutations

    return rank


print(list_position('GADHDDZLDWUESREFUQUFLZL'))  # Output: 1464036526368784298


print(list_position('GADHDDZLDWUESREFUQUFLZL'), 1464036526368784298)
print(list_position('BAAA'), 4)
print(list_position('QUESTION'), 24572)
print(list_position('BOOKKEEPER'), 10743)
