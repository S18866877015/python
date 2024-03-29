import my_tools

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
"""
language = favorite_languages['sarah'][0].title()
print(f"Sarah's favotite language is {language}.")
"""
my_tools.line()

for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}.")

my_tools.line()

for name in favorite_languages.keys():
    print(name.title())

my_tools.line()

for name in favorite_languages:
    print(name.title())

my_tools.line()
"""
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
"""
my_tools.line()
"""
for language in set(favorite_languages.values()):
    print(language)
"""

my_tools.line()

need_poll = ['phil', 'sarah', 'jen', 'edward', 'henry', 'harry']

for name in need_poll:
    if name in favorite_languages.keys():
        print(f"{name.title()} thank you for participating in the survey.")
    else:
        print(f"{name.title()}, please take our poll!")

my_tools.line()

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0]}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")