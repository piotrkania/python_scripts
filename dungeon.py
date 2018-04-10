#!/usr/bin/python
import welcome
import re

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
