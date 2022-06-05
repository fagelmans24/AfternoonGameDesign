#Susie Fagelman
#Pseuodocode:
    #start
    #input instructions 
    #input list of words (colors)
    #import os and random
    #get loop
    #get borders 
    #print instructions
    #get list of colors
    #get randomizer to select a random color from the list
    #input guess a color
    #get user input to guess a random color
    #print "you got it right" if the guess was correct
    #input break if the guess was right
    #print "you got the wrong color" if the guess was wrong
    #input "do you want to play again type yes or no"
    
import random
import os

for i in range(1000): #this keeps the game going 1000 times
    os.system('cls')

    #instructions
    title= 'guessing game!'
    instructions1= 'This is a guessing game where you guess a word from a list.'
    instructions2= 'You have 10 tries to guess the right choice.'
    instructions3= 'If you use all of your guesses and never get the right word, you can just play again!'
    print(title.upper())
    print(instructions1)
    print(instructions2)
    print(instructions3)
    print('=====================================================================================') #here to separate between instructions and game
    print(' ') #this gives a space betwen my instructions and the game

    list= ['red','orange','green','blue', 'yellow', 'purple', 'pink', 'black', 'white', 'navy'] #this is my list of colors that are going to be guessed
    random_color= random.choice(list) #this chooses a random item from the list
    tries= 10 #these are how many tried the player gets
    for i in range(tries): #this allows the player to guess 10 times 
        user_input= input('guess a color: ') #this is the variable where the user inputs their guess
        if user_input==random_color: #this means if the user guessed the correct color then the guessing game ends
            print("you got the color right")
            print("you used",(i+1),"tries")
            break #this stops the loop
        else: #this is for if the player's guess does not equal the random color
            print("you got the wrong color")
            print("you used",(i+1),"tries")
    play_again=input('do you want to play again? Type yes or no ')
    if play_again=='no': #this is for if the player wants to stop playing the loop will end
        print('thanks for playing')
        break
