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

'''
user_value= int(input("enter number"))
for number in range (5, user_value):
    if number % 2 == 1:
        print(number)
'''

''''
def my_func(number):
    number += 2
    number *= 4
    return number
result1 = my_func(10)
result2= my_func(result1)
print(result2)

def add_ten(number):
    number += 10
    return number

result = 10
for number in range(0,10):
    result = my_func(result)
    print(result)

def product(num1, num2):
    product = num1 * num2
    return product
print(product(4,3))
'''

#x = []
lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']
#print(lyst[1])
#print everyting not a string

print(lyst[2:5])
x = 'appl'
print(x)
x += "e"
print(x)

#append(  element  ) will add the element to the end of list
print(lyst)
lyst.append(12)
lyst.insert(2,5) 
print(lyst)
