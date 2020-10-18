# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r')
new_animals = open('animals_new.txt', 'w')
new_animals.write(' '.join(x.rstrip('\n') for x in animals.readlines()))
new_animals.close()
animals.close()
