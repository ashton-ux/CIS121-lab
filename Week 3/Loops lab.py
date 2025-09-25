#Ashton Garcia
'''
larger_num = int(input("Enter Larger number: "))
smaller_num = int(input("Enter Smaller number: "))

num = 0
while larger_num > smaller_num:
    larger_num = larger_num / 2
    num += 1
print(f"Number of times halved: {num}")
'''
# Question 2
'''
word = input("Enter a word: ")
result = ""
for i in range(1, len(word) - 1, 2):
    result += word[i]
print(f"Output = {result}")
'''

#question 3
'''
number = 0
for number in range(37, 1050):
    if number % 2 == 0:
        print(number)
'''
#Question 4
'''
word = ""
while True:
    letter = input("Enter a letter or type done: ")
    if letter == "done":
        break
    else:
        word += letter
print(f"The word is {word}")
'''

#Question 5
'''
number = 0
for sum_number in range(50,517):
    if number % 2 == 1:
        number += sum_number
print(number)
'''
#question 6
total_num = 0
while True:
    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        print(user_num + total_num)
    if user_num < 0:
        break
