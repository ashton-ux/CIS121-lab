# Ashton garcia
'''
def pyramid_volume(base, height):
    volume = (base**2 * height) /3 
    return volume
print(f'The volume of the pyramid is {pyramid_volume(2,2)}')
'''
# Question 8
'''
pool_times == ""
if grade == "k":
    grade = 0

def pool_times(grade, time):
   
    if grade == "K" or (1 < int(grade) < 3):
        if (time == "Morning"):
            pool_times = "9AM"
        else:
            pool_times = "1PM"
    
    return ""
grade = input("Enter your grade: ")
time = input("enter Time: ")
print(F'Pool Time is {pool_times("K, Morning")}')
'''
#Question 11
'''
def convert_knuts(knuts):

    galleons = knuts // (29 * 17)
    remaining_knuts = knuts - (galleons * (29 * 17))

    sickles = remaining_knuts // 29
    remaining_knuts = remaining_knuts % sickles

    output = ""
    if knuts > 0:
        output += f"Knuts: {knuts} "
    if sickles > 0:
        output += f"Sickles: {sickles} "
    if galleons > 0:
        output += f"Galleons: {galleons} "

    return output
print(convert_knuts(544))
'''
#Question 14
'''
from random import randit 
def guess_num(user_guess):
    output = ""
    value = randit(0,9)
    if user_guess == "Even":
        if value % 2 == 0:
            output == "Correct!"
        else:
            output == "Incorrect"
    elif user_guess == "Odd":
        if value % 2 != 0:
            output == "Correct!"
        else:
            output == "Incorrect"

    return output
'''

#Question string quiz 1
def is_fever(temp):
    unit = temp[-1]
    if unit == "F":
        if  float(temp[:-1]) > 98.6:
            return True
        else:
            return False
    if unit == "C":
        if float(temp[:-1]) > 37:
            return True
        else:
            return False
    
user_input = input("Enter temperature in F or C: ")
print(F"Is fever ? {is_fever(user_input)}")
