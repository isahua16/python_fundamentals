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
elif (number >= 0 and is_happy == False):
    print('Positive and False')
elif (number > 100 or is_happy == True):
    print('Large or True')
else:
    print("I don't know")

my_strings = ['One', 'Two', 'Three']
my_numbers = [10, 20, 30]

for string in my_strings:
    print(string)

for number in my_numbers:
    print('Look at this number:', number)

def static_greeting():
    print('Hello Isael')

static_greeting()

def dynamic_greeting(name):
    print(f'Hello, {name}')

dynamic_greeting('Isael')
dynamic_greeting('Daisy')
dynamic_greeting('Amy')


def find_treasure(array):
    for i in array:
        if(i == 'Treasure'):
            return True   
    return False

print(find_treasure(['One', 'Two', 'Three']))
print(find_treasure(['Four', 'Five', 'Treasure']))




