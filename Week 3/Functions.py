lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(x[2])
#print(x[0:4])
#for element in lyst:
#    print(elementt
#print(lyst)
'''
lyst.append('Saturday')
lyst.append('Sunday')
print(lyst[2][3:6])

lyst[4] = 'Funday'
print(lyst)

word = 'apfel'
print(word)
print(word[2])
word[2] = 'p'
print(word)
'''

'''
word_list = ['Peter piper picked a peck of pickled peppers']
result = ["Peter" "piper" "picked" "a" "peck" "of" "pickled" "peppers"]
def string_to_list_vowels(word):
    words = []
    built_word = ''
    vowel_count = 0
    for letter in word:
      print(letter, vowel_count, built_word)
      if letter == ' ':
         if vowel_count >= 2:
            words.append(built_word)
         built_word = '' 
         vowel_count = 0
      else:
         built_word += letter
         if letter in 'aeiou':
            vowel_count += 1
    if vowel_count >= 2:
      words.append(built_word)
    return words
'''

'''
def string_to_list_alt(word):
   words = []
   built_word = ''
   for index in range(len(word)):
      if word[index] == ' ' 
      words.append += word[index]
      built_word = ''
   elif
   else:
      built_word == word[index]
      return words
      index == len(word) -1:''
      '''

#function string as argument returns a dictionary containg all of unique words in string

phonebook = {'matt': 5073891438, 'Ashley': 12365656}
