def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140: return False
    s = s.split()
    s = [x.capitalize() for x in s]
    ans = '#' + ''.join(s)
    return ans


print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice')
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice')
print(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice')
print(generate_hashtag(''), '#CIN')
print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice')
