#Advanced functions
#4 works
'''
def find_winner(player1 = "Rock", player2 = "Rock"):
    if player1 == player2:
        return "its a tie"
    if (player1 == "Rock" and player2 == "Scissors") or (player1 == "Scissors" and player2 == "Paper") or (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 Wins"
    else:
        return "player 2 Wins"



print(find_winner("Rock", "Scissors"))
'''
#question 8
'''
def descending_order(num1, num2 = 15, num3 = 5):
    a = num1
    b = num2
    c = num3
    if a < b < c:
        return c, b, a
    if a < c < b:
        return b, c, a
    else:
        return a, b, c
print(descending_order(30, 50, 100))
print(descending_order(50, 100, 32))
print(descending_order(100, 10, 32))
#sorta works
'''
#13
def is_vowel(letter):
    return letter in ["aeiou"]
def report_vowels(word):
    vowels = []
    for letters in word:
        if is_vowel(letters):
            vowels.append(letters)
        return vowels
    print(report_vowels("apple"))