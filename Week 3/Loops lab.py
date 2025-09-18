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
word = ""
while True:
    letter = input("Enter a letter or type done: ")
    if letter == "done":
        break
    else:
        word += letter
print(f"The word is {word}")