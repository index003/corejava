# 字典中存储列表

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

print(f"You ordered a {pizza['crust']} - crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['go', 'ruby'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")



