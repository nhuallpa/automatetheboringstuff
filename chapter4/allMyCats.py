catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break;
    catNames = catNames + [name]
print('Cat names are:')
for catName in catNames:
    print(' ' + catName)