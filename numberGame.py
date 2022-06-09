#Susie fagelman
#Number Guessing Game
#Pseuodocode: 
# Input user name
# Input menu choices 1 (instructions), 2(1-25), 3(1-50), 4(,1-100), 5(print score), 6 exit
# If user chooses menu choice 1,  Print instructions 
# Input enter to go back to main menu
# User choose 2
# “Pick a random number from 1-25”
# Generate random number 1-25  ->randint(25)+1
# Input a while loop:
# They will have infinite tries
# Input their guesses
# If their guess is the correct number print “congratulations”
# Send the user back to the menu to see their score
# If guess < number 
# print number is more than that
# If guess > number
# 	Print number is less than that
# If they guess the wrong number, they keep guessing until they reach the correct number
# User choose 3: 
# Replace 1-25 with 1-50
# User choose 4:
# Replace 1-50 with 1-100
# If user choose 5:
# Print score
# If user choose 6:
# End game

import numbers
import os
from re import M
os.system ('cls')
import random
import os,datetime



cnt=0

Menu=M #creating variable for menu
Game=True 

name=input ('What is your name?' )
input('Press enter to go to the main menu.' )
while game: #starts loop
    
    os.system ('cls')
    print('Menu:')
    print('   ')
    print('Would you like to go to:') 
    print('1. Instructions') 
    print('2. guessing a number from 1-25')
    print('3. guessing a number from 1-50')
    print('4. guessing a number from 1-100')
    print('5. see you score')
    print ('6. end game')
    guess = True #setting it true so that if user does something wrong we can set it to false
    while guess:
        choice = int(input('Answer as 1,2,3,4,5, or 6.' ))
        try:
            choice=int(choice)
            if choice >0 and choice <7:
                guess = False
                print('Your choice must be from 1-6')
        except:
            print('You must type a number')
        
    if choice==6: #ending game
        print('Come back another time!')
        game=False

    if choice==1:
        os.system('cls')
        #instructions
        print('Welcome to this game',name,'!')
        print('There are three possible levels to choose from:')
        print('Level 1 is guessing a number between 1-25. Level 2 is guessing a number from 1-50 and level 3 is from 1-100')
        print('The higher the level and less guesses it takes you to guess the correct number, the higher your score will be!')
        print('After each guess, you will be told whether your guess is greater or less than the correct number')
        print('Good luck!!')
        input('Press enter to go back to the main menu.' )
    if choice==2: #if the user chooses to play game 2
        max=25 #highest number to choose from
    if choice==3:
        max=50
    if choice==4:
        max=100
    if choice>1 and choice<5: #if the user chooses to play a game
        os.system('cls')
        level1=choice-1
        print("level",level1,":guess a number from 1-", max,".") #making them guess a number from 1 to whatever the max is for that certain game
        num=random.randint(1,max) #choosing random number
        count=0
        stay=True
        while stay and count < max: 
            guess=input('Your guess is:') 
            try:
                guess=int(guess)
                if guess>0 and guess<max+1:
                    if guess==num:
                        stay=False
                        print('Yay you guessed the right number, nice job!')
                        
                    else:
                        print('That number is not the correct number between 1 and',max)
                    if guess >num:
                        print('The number is less than',guess,'.')
                    if guess <num:
                        print('The number is greater than', guess,'.')
                       
                        
                    
            except: #must do except statements if using try
                print('Not a number, must guess a number')
                count +=1
                count==max
                print('You had as many tries as possible number. You are an awful guesser!')
                input('Press enter to go back to menu' )
    
        #scores      
        if choice==5: #takes them to see their score
            score =max-count
            print(name,', your score is',score)
            input('Press enter to move on.' )
            high=0
            if score>high:
                high=score
            two=0
            if score>two and score<high:
                two=score
            three-0      
            if score>three and score<two:
                three=score
            four=0
            if score>four and score<three:
                four =score
            five=0
            if score>five and score<four:
                five = score


            #functions
            date=datetime.datetime.now()
            scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            scrLine2=str(two)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            scrLine3=str(three)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            scrLine4=str(four)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            scrLine5=str(five)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            myFile=open("scre.txt", 'w')
            myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
            myFile.write(scrLine)
            myFile.close()
            myFile=open("scre.txt", 'r') #opens a file to read # lines=myFile.readlines() #need to read entire file
            print()
            for line in myFile.readlines():
             print(line)
            myFile.close()

