'''
number = int(input("enter number: "))
while number >= 5:
    if number % 2 == 1:
        print(number)
    number -= 1
'''

'''
number = 0
while number < 50:
    if number % 2 == 0:
        if number % 3 == 0:
            continue
        print(number)
    number += 1
'''
'''
for number in range (1,11):
    if number % 2 == 0:
        print(number)
'''
user_value= int(input("enter number"))
for number in range (5, user_value):
    if number % 2 == 1:
        print(number)



