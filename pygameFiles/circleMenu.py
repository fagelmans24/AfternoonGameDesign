#Susie fagelman
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

import sys
from turtle import color
import pygame, time,os,random, math
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//22)
screen=pygame.display.set_mode


colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
messageMenu= ["Instructions", "Settings", "Game_1","Game_2","Score","Exit"]
messageSettings=["Background Colors","Screen Size","Sound On/Off"]
Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
#images
bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

#character vars
charx = xb
chary = yb

#circle
cx=350
cy=350
rad=25

#inscribed box
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

#objects to draw
square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
mountainSqaure = pygame.Rect(250, 320, 180, 250)

#collors
squareClr=colors.get("pink")
circleClr=colors.get("blue")
backgrnd=colors.get("white")
buttoncolor= colors.get ("limeGreen")

#Game control
run = True
Game_1 = False
speed=2

#Menu items
message = ["Instructions", "Setting", "Game 1", "Game 2", "Scoreboard", "Exit"]

def menu():
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
    screen.fill(backgrnd)
    ymenu = 155
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))

    Button_Instructions = pygame.Rect(30, 145, 150, 50)
    Button_Settings = pygame.Rect(30, 195, 150, 50)
    Button_Game_1 = pygame.Rect(30, 245, 150, 50)
    Button_Game_2 = pygame.Rect(30, 295, 150, 50)
    Button_Score = pygame.Rect(30, 345, 150, 50)
    Button_Exit = pygame.Rect(30, 395, 150, 50)
    pygame.draw.rect(screen, buttoncolor, Button_Instructions)
    pygame.draw.rect(screen, buttoncolor, Button_Settings)
    pygame.draw.rect(screen, buttoncolor, Button_Game_1)
    pygame.draw.rect(screen, buttoncolor, Button_Game_2)
    pygame.draw.rect(screen, buttoncolor, Button_Score)
    pygame.draw.rect(screen, buttoncolor, Button_Exit)

    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (40, ymenu))
        pygame.display.update()
        pygame.time.delay(50)
        ymenu += 50
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Instructions.collidepoint((mx, my)):
                    Instructions("Instructions" , "pygameFiles\instructions.txt")
                if Button_Settings.collidepoint((mx, my)):
                    settings ()
                if Button_Game_1.collidepoint((mx, my)):
                    Game_1 ()
                if Button_Game_2.collidepoint((mx, my)):
                    Game_1 ()
                if Button_Score.collidepoint((mx, my)):
                    Instructions ("Highscores", "python folder\scre.txt")
                if Button_Exit.collidepoint((mx, my)):
                    pygame.quit ()
                    sys.exit ()

def Instructions(TITLE, FILE):
    #rendering text objects
    Title = TITLE_FONT.render(TITLE, 1, colors.get("blue"))
    
    #fills screen with white
    screen.fill(backgrnd)


    #Instructions
    myFile = open(FILE, "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu ()
                print("Y quit")
           
                


def settings ():
    global WIDTH, HEIGHT, backgrnd, screen, buttoncolor
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
    screen.fill(backgrnd)
    ymenu = 155
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    
    Bx= WIDTH//3

    Button_Color = pygame.Rect(Bx, 150, WIDTH//4, 40)
    Button_Background = pygame.Rect(Bx, 200, WIDTH//4, 40)
    Button_Sizeincrease= pygame.Rect(Bx, 250, WIDTH//4, 40)
    Button_Sizedecrease= pygame.Rect(Bx, 300, WIDTH//4, 40)
    
    
    pygame.draw.rect(screen, buttoncolor, Button_Color)
    pygame.draw.rect(screen, buttoncolor, Button_Background)
    pygame.draw.rect(screen, buttoncolor, Button_Sizeincrease)
    pygame.draw.rect(screen, buttoncolor, Button_Sizedecrease)
    
    color = MENU_FONT.render("Randomize button color", 1, colors.get("blue"))
    bgcolor = MENU_FONT.render("Randomize background color", 1, colors.get("blue"))
    sizeincrease = MENU_FONT.render("Increase screen size",1, colors.get ("blue"))
    sizedecrease = MENU_FONT.render("Decrease screen size",1, colors.get ("blue"))

    screen.blit(color, (WIDTH//2 - (color.get_width()//2), 160))
    screen.blit(bgcolor, (WIDTH//2 - (bgcolor.get_width()//2), 210))
    screen.blit(sizeincrease, (WIDTH//2 - (sizeincrease.get_width()//2), 260))
    screen.blit(sizedecrease, (WIDTH//2 - (sizedecrease.get_width()//2), 310))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu ()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if Button_Color.collidepoint(mx,my):
                    buttoncolor=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
                    
                if Button_Background.collidepoint(mx,my):
                    backgrnd=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
                if Button_Sizeincrease.collidepoint(mx, my):
                    WIDTH+=100
                    screen= pygame.display.set_mode((WIDTH,HEIGHT))
                if Button_Sizedecrease.collidepoint(mx, my) and WIDTH >500:
                    WIDTH -=100
                    screen= pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.update()
            settings()
                
                    
                
     


def Game_1 ():
    global run, insSquare, charx, chary, cx, cy, rad
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu ()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                # print(mousePos)
        
        pygame.draw.rect((screen, backgrnd), mountainSqaure)
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        if square.colliderect(mountainSqaure):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)

        pygame.display.update()

        

menu ()