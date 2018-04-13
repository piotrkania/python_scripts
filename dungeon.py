#!/usr/bin/python
import welcome
import re

#Greetings

print """
You yawn widely, and scratch Your head.
 'Where am I? What happend last night? I can't remember anything...
  Last moment, last thing that I remember was this...person...thing...
  Who or what was that?'
"""



# Function to provide characters race
def char_race():
    race_list=['Orc','Human','Elf','Dwarf']
    while True:
        race=raw_input("Please select Your race (Orc/Elf/Human/Dwarf): ")
        if race.isalpha() and race in race_list:
            if race=='Orc':
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
	    elif race=='Elf':
                print "You are an elf"
            return race
            break
        else:
            print "You must choose a valid race!"
            continue


char_race()

# Function to provide character  name
def char_name():
    while True:
        name=raw_input("Whats Your name? :")
        if name.isalpha():
            #print "Hello " + name + " !"
            return name
            break
        else:
            print "You must type letters! Try again..."
            continue

char_name()

# Function to choose first room
def first_room():
    while True:
        first_room={
        'Left': 'Military quarters',
        'Center': 'Cellar',
        'Right': 'Servants quarters'
}
        direction=raw_input("Where would You like to go? (Left/Right/Center): ")
        for key in first_room.items():
            if direction in first_room:
                if direction=='Left':
                    print "You enter " + first_room[direction] + "." + " Watch out for undead troops!!!"
                elif direction=='Right':
                    print "You enter " + first_room[direction] + "." + " Something or someone can eat You here...Watch Your back..."
                elif direction=='Center':
                    print "You enter " + first_room[direction] + "." + " Whats crawling below?"
                #print first_room[direction]
                return first_room[direction]
                break
            else:
                print "Wrong direction, choose again..."
                continue

first_room()


print "You encounter a zombie"
import dice_roll
