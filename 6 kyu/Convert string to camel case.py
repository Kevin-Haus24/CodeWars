def to_camel_case(text):
    text = text.replace('_', '-').split('-')
    for i in range(1, len(text)):
        text[i] = text[i].title()
    return ''.join([x for x in text])


print(to_camel_case(""), "")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
print(to_camel_case("A-B-C"), "ABC")