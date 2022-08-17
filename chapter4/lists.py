
# Multi assignment trick
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

# Enumerate
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Random choice() and random.shuffle()
import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)

# Augmented Assignment Operator
spam = 42
spam += 1
spam -= 1
spam *= 1
spam /= 1
spam %= 1
spam = 'Hello'
spam += ' world!'
print(spam)
bacon = ['Zophie']
bacon *= 3
bacon

## METHODS
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('heyas')

#  Modify the list in place
spam.append('hey')
spam.insert(1, 'che')
spam.remove('hi')

# Sorting in place, and doesn't return a list
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam.sort(reverse=True)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()   # ASCIIbetical order
spam.sort(key=str.lower)  # Alphabetical order

spam = ['cat', 'dog', 'moose']
spam.reverse()

## Secuence Data Type
name = 'Santiago'
name[0]
name[0:5]
'Sant' in name
for i in name:
    print("* * * * * " + i +" * * * * *")

