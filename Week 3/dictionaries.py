#Dictionaires
'''
def get_names(my_dict):
    names = []
    #1. iterate through list
    for key in my_dict:
        #2. access value in key
        name = my_dict[key]
        #3. put names in list
        names.append(name)
    return names

names_dict = {"01234": "Steve", "9876": "Alice", "564656561": "Bob"}
print(get_names(names_dict))
'''

#Question 5
''''
def find_oldest(persons):
    oldest_person = []
    max_age = -1

    for name in persons:
        age = persons[name]
        if age > max_age:
            max_age = age
            oldest_name = name
    return  oldest_name  


persons = {"Emma": 71, "Jack": 45}
print(find_oldest(persons))
'''


# 6
def letter_count(word):
    count_dict = {}
    for letter in word:
        if letter not in count_dict:
           count_dict[letter] = 1
        else:
            count_dict[letter] += 1

    return count_dict


print(letter_count("Mississippi"))

'''
def unique_num(number):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.
    array = {}
    for num in number:
'''     