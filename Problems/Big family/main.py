# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
big_family = dict()
for d in (first_family, second_family):
    for key, value in d.items():
        big_family[key] = value

print(big_family)
