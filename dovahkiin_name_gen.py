#Melody Coleman
#Program allows sorting dragon words by syllable and produces random dragon names.
#PYTHON 2.7

import random


#Definitions
#bool, checks if word is one syllable or not
def oneSyl(s):
    isOne = False
    count = 0
    prev = False
    
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels and prev == False:
            count += 1
            prev = True
        elif ch not in vowels and prev == True:
            prev = False
        elif ch in vowels and prev == True:
            #don't count it, catches names like Vaa. Still counts as 1
            prev = False
            
    if count == 1:
        isOne = True
    
    return isOne
    
#Reads the data into dictionary structure
#Load for Name: reads in only 1 syllable words of the following categories:
#noun, verb, adjective, preposition, adverb
def printAll():
    names = {}
    with open("dragonwords.txt") as file:
        for line in file:
            tokens = line.strip().split("\t")
            
            #If word is one syllable and part of one of the categories... add it
            if oneSyl(tokens[0]) and (tokens[1] == "noun" or tokens[1] == "verb" or tokens[1] == "adjective" or tokens[1] == "preposition" or tokens[1] == "adverb"):
                info = {}
                info['Type'] = tokens[1]
                info['Canon'] = tokens[2]
                info['Definition'] = tokens[3]
                print tokens[0], " ", tokens[3]
                names[tokens[0]] = info
    file.close()
    quit()

#Reads the data into dictionary structure
#Load for Name: reads in only 1 syllable words of the following categories:
#noun, verb, adjective, preposition, adverb
def loadGenerator():
    names = {}
    with open("dragonwords.txt") as file:
        for line in file:
            tokens = line.strip().split("\t")
            
            #If word is one syllable and part of one of the categories... add it
            if oneSyl(tokens[0]) and tokens[2] == 'Canon' and (tokens[1] == "noun" or tokens[1] == "verb" or tokens[1] == "adjective" or tokens[1] == "preposition" or tokens[1] == "adverb"):
                info = {}
                info['Type'] = tokens[1]
                info['Canon'] = tokens[2]
                info['Definition'] = tokens[3]
                names[tokens[0]] = info
    file.close()
    return names

def generate(names, num):
    for i in range(0,num):
        name1 = random.choice(names.keys())
        name2 = random.choice(names.keys())
        name3 = random.choice(names.keys())
        print name1, name2, name3
        print names.get(name1).get('Definition'), "//", names.get(name2).get('Definition'), "//", names.get(name3).get('Definition'), "\n"
        
def intInput(inquiry):
    while 1:
        try:
            num = int(input(inquiry))
        except ValueError:
            print("Please type a number. ")
            continue
        else:
            return num
            break
    

#Prompt user for how to load the dictionary
while (1):

    sel = intInput("Please type the number for your selection:\n(1) Loads all one syllable dragon words for making dragon names.\n(2) Generates a standard three-syllable dragon name and gives definition.\n")
    
    #If 1 or 2 is selected
    if sel == 1:
        printAll()
    
    #If user is loading all
    elif sel == 2:
        nmbr = intInput("How many do you want generated? ")
        if nmbr > 50:
            nmbr = 50
        elif nmbr < 1:
            nmbr = 1
        
        generate(loadGenerator(), nmbr)
        quit()

    #if input invalid
    else:
        print "Please type the numeric value 1 or 2"