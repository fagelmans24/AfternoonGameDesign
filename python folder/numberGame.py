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


import os
from tkinter import Menu

os.system ('cls')
import random
import os,datetime

def printinstructions():
    myFile=open('python folder/NUmberGameInstructions.txt','r')
    stuff=myFile.readlines()
    myFile.close()
    for line in stuff:
        print(line)


def scoreboard(): # this function displays the top 5 scores
    myFile = open("python folder/NumberGamescre.txt","r")
    score = myFile.readlines()
    score.sort(reverse=True)
    myFile.close()
    x=1
    for line in score:
        print(line)  
        x+=1
        if x == 5:
            break


def createguesssinggame(range, tries): # this function creates the guessing game #
    random_number = random.randint(1, range)
    cnt = 0
    score = 0
    while cnt < tries: 
        cnt +=1       
        while True:
            player_guess = input("Enter a number between 1 and "+str(range)+": ")
            try:
                player_guess = int(player_guess)
                if player_guess > 0 and player_guess < range+1:
                    break
                else:
                    print("Guess a number in between 1 - "+str(range))
            except:
                print("That is not a number. Plese enter a number:")
        if player_guess == random_number:
            print("Nice, you guessed the correct number in "+str(cnt)+" tries")           
            score = 50*(tries+1 - cnt)
            print("your score is "+str(score)) 
            break
        if cnt == tries and player_guess != random_number:
            print("Sorry you didn't guess the correct number in time :(")
            break
        if player_guess != random_number:
            if player_guess > random_number:
                print("Your guess is greater than the number")
                print("you have " + str(tries-cnt) + " tries left")  
            else:
                print("Your guess is less than the number ")    
                print("you have " + str(tries-cnt) + " tries left")            
    return score  


Highscore=0
Game=True 

name=input ('What is your name?' )
input('Press enter to go to the main menu.' )
while Game: #starts loop
    
    os.system ('cls')
    print('Menu:')
    print('   ')
    print('Would you like to go to:') 
    print('1. Instructions') 
    print('2. Guessing a number from 1-25')
    print('3. Guessing a number from 1-50')
    print('4. Guessing a number from 1-100')
    print('5. See you score')
    print ('6. End game')

    guess = True #setting it true so that if user does something wrong we can set it to false
    while guess:
        choice = int(input('Answer as 1,2,3,4,5, or 6.' ))
        try:
            choice=int(choice)
            if choice >0 and choice <7:
                guess = False
            else: 
                print('Your choice must be from 1-6')
        except:
            print('You must type a number')
        
    if choice==6: #ending game
        print('Come back another time!')
        Game=False


    if choice==1:
        os.system('cls')
        printinstructions() 
        input('Press enter to go back to menu.')

        

    if choice==2: #if the user chooses to play game 2 #highest number to choose from
        os.system('cls')
        score = createguesssinggame(25,6)
        input("Press enter to go back to menu: ")
        if score>Highscore:
            Highscore=score
    if choice==3:
        os.system('cls')
        score = createguesssinggame(50,8)
        if score>Highscore:
            Highscore=score
        input('Press enter 5to go back to menu: ')
    if choice==4:
        os.system('cls')
        score = createguesssinggame(100,10)
        if score>Highscore:
            Highscore=score
        input("Press enter to go back to menu: ")
            
    if choice==5: #takes them to see their score
            print(scoreboard())
            input('Press enter to go back to Menu')

            # #files
            # date=datetime.datetime.now()
            # scrLine=str(high)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            # scrLine2=str(two)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            # scrLine3=str(three)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            # scrLine4=str(four)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            # scrLine5=str(five)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
            # myFile=open("scre.txt", 'w')
            # myFile.write(scrLine+scrLine2+scrLine3+scrLine4+scrLine5)
            # myFile.write(scrLine)
            # myFile.close()
            # myFile=open("scre.txt", 'r') #opens a file to read # lines=myFile.readlines() #need to read entire file
            # print()
            # for line in myFile.readlines():
            #  print(line)
            # myFile.close()

date = datetime.datetime.now()
scrLile=str(Highscore)+"\n"
# "\t"+date.strftime('%m / %d/ %y')+"\t"+name +
myFile=open("python folder/numberscore.txt", 'a')
myFile.write(scrLile) # adds the score to the game
myFile.close()  

