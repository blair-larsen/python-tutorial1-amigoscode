
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + 'is walking...')

    def speak(self):
        print('Hello my name is ' + self.name + ' and I am' + str(self.age) + ' Years old')

    
john = Person('John', 22)
me = Person('Blair',100)

print(john.name + ':' + str(john.age))
john.speak()
john.walk()

print("-----------------")

me = Person('Blair',100)
print(me.name + ':' + str(me.age))
me.speak()
me.walk()

"""
def check_age(age):
    if age < 18:
        return 'fun: opps not an adult'
    else:
        return 'fun: an adult'

print("checking 17: " + check_age(17))

print('hello'.upper())
#check_age(17)

first_name = 'blair'
age = 22

cars = ['bwm', 'vw', 'tesla']


surname = 'Larsen'
full_name = first_name.capitalize() + ' ' + surname
print(full_name)

print(len(first_name))
print(len(surname))

print(full_name.endswith('hello'))  # False

addition = 10 % 3
print(addition)

# boolean
print(10 <= 10)
print(0 == 1)
print(18 > 5)
print('blair'.endswith('x'))
print('blair'.endswith('r'))

is_adult = False
age = 18
if not is_adult:
    print("adult")

if age > age:
    print("is adult")
else:
    print("not adult")



cars = ['bmw','vw','tesla']
print(len(cars))
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())

    print("blair".capitalize)

    number = 0
    while number <= 10:
        print(number)
        number += 1
    else:
        #print('loop done number:' + str(number))
        print('loop ended:', number)
"""

