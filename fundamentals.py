number = 101
string = 'Daisy'
is_happy = True
print(number, string, is_happy)

if (number > 10):
    print('The number is larger than 10')
else:
    print('The number is less than 10')

if (number < 0 and is_happy == True):
    print('Negative and True')
elif (number > 0 and is_happy == False):
    print('Positive and False')
elif (number > 100 or is_happy == True):
    print('Large or True')
else:
    print("I don't know")


