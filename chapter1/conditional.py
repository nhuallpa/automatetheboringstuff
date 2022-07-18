name = 'Mary'
password = 'swordfish'
age = 3000
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Access denied')
        
if name == 'Alice':
    print('Hello, Alice')
elif age < 12:
    print('You are not alice, kiddo')
else:
    print('You are neither Alice nor a little kid.')