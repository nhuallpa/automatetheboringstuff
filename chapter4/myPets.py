pets=['Cacho', 'Buddy', 'Bob']
print('Enter a pet name')
name=input()
if name not in pets:
    print("I don't have a pet name " + name)
else:
    print(name + " is my pet.")
