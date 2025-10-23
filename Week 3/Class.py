'''
import math
class Planet:
    def __init__ (self, _name, _radius, _mass, _distance):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance
        
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    def set_name(self, new_name):
        self.name = new_name


planet1 = Planet("Venus", 45 ,198, 1000)
planet2 = Planet("Uranus", 12, 234, 2381)

print(planet1.get_mass())
print(planet2.get_density())
print(planet1.get_name())
planet1.set_name("x25")
print(planet1.get_name())
'''
#13
def is_vowel(letter):
    # Check if the letter is a vowel (case-insensitive)
    return letter in ['a', 'e', 'i', 'o', 'u']

def report_vowels(text):
    vowels = []
    for char in text:
        if is_vowel(char):
            vowels.append(char)
    return vowels
print(report_vowels("apple"))          # Output: ['a', 'e']
print(report_vowels("banana"))         # Output: ['a', 'a', 'a']
print(report_vowels("run time error")) # Output: ['u', 'i', 'e', 'e', 'o']
def is_vowel(letter):
    return letter in ["a","e","i","o","u"]
def report_vowels(word):
    vowels = []
    for i in word:
        if is_vowel(i):
            vowels.append(i)
    return vowels
print(report_vowels("apple"))