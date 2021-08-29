favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

alien_0 = {
    'color': 'green',
    'points': 5
}

speed_value = alien_0.get('speed', "No speed value assigned.")
print(speed_value)
speed_value = alien_0.get('speed')
print(speed_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# items()不可以忘记了
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}")

for name in favorite_languages.keys():
    print(f"\t{name.title()}")

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"\tHi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# sorted排序并且不改变原有顺序
for name in sorted(favorite_languages.keys()):
    print(f"\t{name.title()}, thank you for taking the poll!")

for language in favorite_languages.values():
    print(language.title())

# set去重
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")
