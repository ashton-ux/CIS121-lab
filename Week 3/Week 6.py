# QUESTION 5
def hailstone_seq(number):
    output_list = []

    while number != 1:
        if number % 2 == 0:
        # even
            number /= 2
        else:
            # odd
            number = (3 * number) + 1
        print(number)
        output_list.append(number)
    return output_list
result = hailstone_seq(25)

for num in result:
    print(f'{num}')


# QUESTION 9 blackjack
'''
def count(lst_of_cards):
    points = 0
    for card in lst_of_cards:
        temp_card = str(card)
        #2,3,4,5,6 = +1
        if temp_card in ["2", "3", "4", "5", "6"]:
            points += 1 
        # 10, j, q, k = -1
        elif temp_card in ["10", "j", "q", "k", "a"]:
            points -= 1 

    return points

Deck1 = [5,9, 10, 3, "j", "a", 4, 8, 5]
Deck2 = ["a", "a", "k", "q", "q", "j"]

print(f"Total points Deck 1: {count(Deck1)}")
print(f"Total points Deck 1: {count(Deck2)}")
'''

# QUESTION 19
def is_acronym(s, words):
    #if len of s != words -> false
   
    if len(s) != len(words):
        return False
    for i in range(0, len(words)): 
        # if word == '' -> false
        current_words = words[i]
        if current_words == '':
            return False

        if words[i] =="":
            return False
    if s[i] != words [i][0]:

    
    
    
s = "abc"    
words = ["alice", "bob", "charlie"]





    return True 