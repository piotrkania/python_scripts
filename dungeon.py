#!/usr/bin/python
import welcome
import re
from random import randint



# Class to define die roll
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

# Die-type definitions

four_sided_die=Die(4)
six_sided_die=Die(6)
ten_sided_die=Die(10)

# Function to provide characters race
def char_race():
     race_list=['Orc','Human','Elf','Dwarf']
     while True:
        race=raw_input("Please select Your race (Orc/Elf/Human/Dwarf): ")
        if race.isalpha() and race in race_list:
            return race
        else:
            print "You must choose a valid race!"
            continue

# Function to provide character  name
def char_name():
    while True:
        name=raw_input("Whats Your name? :")
        if name.isalpha():
            return name
        else:
            print "You must type letters! Try again..."
            continue

# Function to choose first chamber
def first_chamber():
    while True:
        first_chamber={
        'Left': 'Military quarters. Watch out for undead troops!!!',
        'Center': 'Cellar. Something or someone can eat You here...Watch Your back...',
        'Right': 'Servants quarters. Whats crawling below?'
}
        direction=raw_input("Where would You like to go? (Left/Right/Center): ")
        for key in first_chamber.items():
            if direction in first_chamber:
                return first_chamber[direction]
                print first_chamber[direction]
            else:
                print "Wrong direction, choose again..."

# MONSTER CLASSES
#This section defines the general monster class

class Monster:
    def __init__(self,name,hp,ac,exp,atk):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.exp=exp
        self.atk=atk

class Zombie(Monster):
    def __init__(self):
        super().__init__(name="Zombie",
                         hp=10,ac=5,
                         exp=5,atk=4)

class Ghul(Monster):
    def __init__(self):
        super().__init__(name="Ghul",
                         hp=12,ac=6,
                         exp=4,atk=5)

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name="Skeleton",
                         hp=6,ac=2,
                         exp=2,atk=2)

class Ghost(Monster):
    def __init__(self):
        super().__init__(name="Ghost",
                         hp=5,ac=10,
                         exp=6,atk=2)
	
#Greetings
char_name()



print """
You yawn widely, and scratch Your head.
 'What happend yesterday? I can't remember anything...
  Last moment, last thing that I remember was this...person...thing...
  Who or what was that?'
"""


# Race selection

var_race=char_race()
if var_race=='Orc':
    print """



You see an old Orc Shaman, with only one eye.
He's old, very old, even for orcish standards.
'You come, me got gift for you' - screamed the old Orc.
A sudden an unknown curiosity forced You to move towards him.
'You take, no ask'
The same curiosity told You to take the gift - strange looking key,
with an orcish little skull.
'You know where, You sleep now' yelled the Shaman and when You started
to realize whats happening, darkness came and You fell asleep.
You woke up, near a strange looking mansion, with a key in Your pocket.
'What the hell is going on?'
Driven by the same feeling You had earlier, You take Your axe and start
walking towards the building.




"""
elif var_race=='Elf':
    print "Elivsh"
elif var_race=='Dwarf':
    print "Dwarvish"
elif var_race=='Human':
    print "Humanish"
# Enter the building
while True:
    start=raw_input("Hit 'Enter' to enter the building: ")
    if start=="":
        print "You slowly enter the mansion"
        break
    else:
        print "Are You sure You dont't want to know whats behind the door ?"
        continue

# Events based on first chamber selection

var_firstChamber=first_chamber()
print var_firstChamber
