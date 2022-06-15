#Susie Fagelman
#Tic Tac Toe

# functions:
# draw_grid()
#zero_grid()
#draw_markers()
#check_winner()
#game_end()

import os, random, time, pygame, math, datetime,sys
os.system('cls')

pygame.init()

TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}

clr=colors.get("limeGreen")
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Colors", "Screen Size", "Sound On/Off"]
mainTitle="Circle eats Square Menu"
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Tic Tac Toe")  #change the title of my window
backgrnd=colors.get("pink")

#game Variable
player=1
markers=[]
lineWidth=10
Game=True
MxMy=(0,0)
print(markers)  
cirClr=colors.get("blue")
xClr=(0,0,0)
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)


def draw_grid():
    lineClr=colors.get("white")
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Horizontal line
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vertical line
    pygame.time.delay(100)

def draw_Markers():
    xValue=0
    for x in markers:   # getting a row
        yValue=0
        for y in x:  #each element in the row
            if y ==1:
                # print ("x")
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                # print("O")
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update() 
def checkWinner():
    if markers[0][0]+markers[0][1]+markers[0][2]==3:
        print("X won!")
    elif markers[0][0]+markers[0][1]+markers[0][2]==-3:
        print("Y won")
    elif markers[1][0]+markers[1][1]+markers[1][2]==3:
        print("X won!")
    elif markers[1][0]+markers[1][1]+markers[1][2]==-3:
        print ("Y won")
    elif markers[2][0]+markers[2][1]+markers[2][2]==3:
        print ("X won!")
    elif markers[2][0]+markers[2][1]+markers[2][2]==-3:
        print("Y won")
    elif markers[0][0]+markers[1][0]+markers[2][0]==3:
        print("X won!")
    elif markers[0][0]+markers[1][0]+markers[2][0]==-3:
        print ("Y won")
    elif markers[0][1]+markers[1][1]+markers[2][1]==3:
        print("X won!")
    elif markers[0][1]+markers[1][1]+markers[2][1]==-3:
        print("Y won!")
    elif markers[0][2]+markers[1][2]+markers[2][2]==3:
        print ("X won!")
    elif markers[0][2]+markers[1][2]+markers[2][2]==-3:
        print ("Y won!")
    elif markers[0][0]+markers[1][1]+markers[2][2]==3:
        print ("X won!")
    elif markers[0][0]+markers[1][1]+markers[2][2]==-3:
        print("Y won!")
    elif markers[2][0]+markers[1][1]+markers[0][2]==3:
        print("X won!")
    elif markers[2][0]+markers[1][1]+markers[0][2]==-3:
        print ("Y won!")
    elif markers[0][0] != 0 and markers[0][1] != 0 and markers[0][2] != 0 and markers[1][0] != 0 and markers[1][1] != 0 and markers[1][2] != 0 and markers[2][0] != 0 and markers[2][1] != 0 and markers[2][2] != 0:
        print("Tied!")
    
    #winner =1
    
def gameEnd():
    print()
zero_Array()
while Game:
    screen.fill(backgrnd)
    draw_grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            print(cellx, celly)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
            
        
            
    pygame.display.update() 
    pygame.time.delay(100)

