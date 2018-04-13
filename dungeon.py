#!/usr/bin/python
import welcome
import re

#Greetings

print """
You yawn widely, and scratch Your head.
 'What happend yesterday? I can't remember anything...
  Last moment, last thing that I remember was this...person...thing...
  Who or what was that?'
"""



# Function to provide characters race
def char_race():
    race_list=['Orc','Human','Elf','Dwarf']
    while True:
        race=raw_input("Please select Your race (Orc/Elf/Human/Dwarf): ")
        if race.isalpha() and race in race_list:
            #print "You are " + race + " !"
            return race
            break
        else:
            print "You must choose a valid race!"
            continue


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


# Function to provide character age
def char_age():
    while True:
        age=raw_input("How old are You? :")
        if age.isdigit():
            #print "You are " + age + " !"
            return str(age)
            break
        else:
            print "You must type digits! Try again..."
            continue

print "Greetings " + "," + char_race() + " "  +  char_name() + " ! " + "You are " + char_age() + " years old" +  "."

# Function to choose first chamber
def first_chamber():
    while True:
        first_chamber={
        'Left': 'Military quarters',
        'Center': 'Cellar',
        'Right': 'Servants quarters'
}
        direction=raw_input("Where would You like to go? (Left/Right/Center): ")
        for key in first_chamber.items():
            if direction in first_chamber:
                if direction=='Left':
                    print "You enter " + first_chamber[direction] + "." + " Watch out for undead troops!!!"
                elif direction=='Right':
                    print "You enter " + first_chamber[direction] + "." + " Something or someone can eat You here...Watch Your back..."
                elif direction=='Center':
                    print "You enter " + first_chamber[direction] + "." + " Whats crawling below?"
                #print first_chamber[direction]
                return first_chamber[direction]
                break
            else:
                print "Wrong direction, choose again..."
                continue

first_chamber()

