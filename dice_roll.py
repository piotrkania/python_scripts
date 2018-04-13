#!/usr/bin/python

from random import randrange

diceAmountType = raw_input("Enter dice amount and type as XdX: ")
print (diceAmountType)
print '\n'
diceAmount = diceAmountType.split("d", 1)[0]
diceType = int(diceAmountType.split("d", 2)[1])
total = 0
rollSum = 0
natOnes = 0
natTwenties = 0

for x in range(1, (int(diceAmount) + 1)):
    roll = randrange(1, (diceType) + 1)
    totalRoll = roll 
    if diceType == 20:
        if roll == 1:
                natOnes += 1
                print "Roll " + str(x) + ": " + "Natural 1 " + str(roll)
        elif roll == 20:
                natTwenties += 1
                print "Roll " + str(x) + ": " + "Natural 20! " + str(roll)
        else:
                print "Roll " + str(x) + ": " + str(totalRoll) + str(roll)
    else:
        print "Roll " + str(x) + ": " + str(totalRoll) + str(roll)
    rollSum = rollSum + roll
    total = total + totalRoll
print '\n'
print "Total: "+ str(total) + str(rollSum)
if diceType == 20:
        print ("Natural 1's: " + str(natOnes))
        print ("Natural 20's: " + str(natTwenties))
