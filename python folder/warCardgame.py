# Susie Fagelman
# Pseudocode:
# Create a while loop that runs 50 times
# Check if player lists length is 0, if the list is 0 end the game and the player loses (break loop)
# Find length of deck and check if player is at end of deck
# If at the end of the deck go back to the start of the list
# Create a new variable that does not have the last two characters (sign and ‘ , ’ )
# Create integer values for K (king) Q (queen) J (jack) and A (ace)
# Compare the value of player 1 card to player 2 card 
# If player 1’s card is greater than player 2’s add player play 2’s card onto player 1’s deck 
# Else add player 1’s card to play 2’s deck 
# After loop runs 50 times check the length of play 1 and player 2’s deck, the player with the longest list wins 



#first let's import random procedures since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]
    

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase

    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make

    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            # print(deck[counter], end=" ")
            counter +=1
        # print()
    #now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    player1=[]
    player2=[]
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])
    # print("player1 ",player1)
    # print()
    # print("player2 ",player2)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
    return player1, player2    
create_DECK()
decs = playerCards()
player1 = decs[0]
player2 = decs[1]

count = 1 
p1_deckcount = 0
p2_deckcount = 0
while count < 50: #starts the loo[]
    if len(player1) == 0: #this means that if player 1 has no cards left they lose 
        print("Player 1 lost!")
        break
    if len(player2) == 0:
        print("Player 2 loses")
        break
    if p1_deckcount > len(player1)-1:
        p1_deckcount = 0
    if p2_deckcount > len(player2)-1:
        p2_deckcount = 0

    player1_card = player1[p1_deckcount]  
    player1_card = player1_card[0:len(player1_card)-3]  
    if player1_card == "J": #this is just defining what each letter is worth in cards 
        player1_card = 11
    if player1_card == "Q":
        player1_card = 12
    if player1_card == "K":
        player1_card = 13
    if player1_card == "A":
        player1_card = 14        

    player2_card = player2[p2_deckcount]  
    player2_card = player2_card[0:len(player2_card)-3]  
    if player2_card == "J":
        player2_card = 11
    if player2_card == "Q":
        player2_card = 12
    if player2_card == "K":
        player2_card = 13
    if player2_card == "A":
        player2_card = 14 

    if int(player1_card) > int(player2_card):  #this is saying that if player 1's card is greater than player 2, the card is added into player one's stack
        player1.append(player2[p2_deckcount])
        player2.remove(player2[p2_deckcount])

    elif int(player2_card) > int(player1_card):
        player2.append(player1[p1_deckcount])
        player1.remove(player1[p1_deckcount])

    if count == 49: #if it has run 49 times then it shows each players cards 
        print("Player 1's cards:",player1)
        print()
        print("Player 2's cards:" , player2)
        print()
        if len(player1) > len(player2): #if player 1 has more cards than player 2 after 50 plays, they win 
            print("Congrats Player 1, you won!")  
        elif len(player1) < len(player2):
            print("Congrats Player 2, you won!") 
        else:
            print("Both players tied.")        
    
    p1_deckcount +=1
    p2_deckcount +=1
    count +=1