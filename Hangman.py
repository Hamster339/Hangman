#Hamish Philip

import random
from nltk.corpus import words
Words = words.words()

def update_pic(Display_line,disgard,lives):
    if lives == 8:
        print("__________")
    elif lives == 7:
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|______")
    elif lives == 6:
        print("    _____")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|______")
    elif lives == 5:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |")
        print("   |")
        print("___|______")
    elif lives == 4:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |    |")
        print("   |")
        print("___|______")
    elif lives == 3:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |  --|")
        print("   |")
        print("___|______")
    elif lives == 2:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |  --|--")
        print("   |")
        print("___|______")
    elif lives == 1:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |  --|--")
        print("   |   /    ")
        print("___|______")
    elif lives == 0:
        print("    _____")
        print("   |    |")
        print("   |    0")
        print("   |  --|--")
        print("   |   / \   ")
        print("___|______")

    print(" ".join(Display_line))
    print(" ".join(Disgard))
    
def choose_letter():
    global lives
    global Ran_word
    global Display_line
    global Disgard
    
    Correct = False
    while not Correct:
        letter = input("Please enter letter").lower()
        
        if len(letter) == 1:
            
            try:
                int(letter)
            except:
                if letter not in Disgard:
                    Correct = True
                else:
                    print("letter already used")
            else:
                print("you cannot enter a number")
        else:
            print("Just one letter")
   
    found = False
    for charicter in range(0,len(Ran_word)):
        if letter == Ran_word[charicter]:
            Display_line[charicter] = letter
            if letter not in Disgard:
                Disgard.append(letter)
            found = True
            
                
    if found == False:
        Disgard.append(letter)
        lives = lives - 1
        
go = True
while go == True:           

    lives = 8
    Ran_word = Words[random.randint(0,len(Words)-1)]
    Disgard = ["Used: "]
    Display_line = []

    for x in range(0,len(Ran_word)):
        Display_line.append("_ ")

    input("Welcome to hangman! press enter to start.")

    Game = True
    while Game == True:
        Win = True
        update_pic(Display_line,Disgard,lives)
        choose_letter()
        
        for charicter in range(0,len(Display_line)):
            if Display_line[charicter] == "_ ":
                Win = False
        
        if Win == True:
            Game = False
            Win = True
            update_pic(Display_line,Disgard,lives)
            print("You won!")
        
        if lives == 0:
            Game = False
            update_pic(Display_line,Disgard,lives)
            print("You lost :( the word was", "".join(Ran_word))
    
    correct = False
    while correct == False:
        choice = input("Do you wish to play again? Y or N: ")
        
        if choice.upper() == "N":
            go = False
            correct = True
        elif choice.upper() == "Y":
            correct = True
        else:
            print("Please only enter Y or N")
            
            
        
        

        

