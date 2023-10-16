from collections import Counter
def duplicate_count(text):
    test = text.lower()
    count = dict(Counter(test))
    key = count.keys()
    ans = 0
    for i in key:
        if count[i] > 1:
            ans += 1
    return ans

print(duplicate_count(""), 0)
print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdeaa"), 1)
print(duplicate_count("abcdeaB"), 2)
print(duplicate_count("Indivisibilities"), 2)