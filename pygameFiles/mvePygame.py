#Susie Fagelman
#6/9/2022
#We are learning pygame basic functions
#creating screens, clrs, shape
# #K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
# K_INSERT              insert

import squrt
from msvcrt import kbhit
from random import random
from turtle  import speed, width 
import random
import pygame, time, os
pygame.init() #initialize the pygame package
colors={"white":(255,255,255),"pink":(255,0,255), "blue":(0,0,255),"limeGreen":(153,255,51)}
WIDTH=700 #like a constant 
HEIGHT=700
#create display window with anyname you like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #set_mode is how big you want the thing
pygame.display.set_caption("My First Game") #changes the title of my window
clr=colors.get('limeGreen')
# greenClr=(0,255,0)
# purpleClr=(125,0,125)
# # screen.fill(greenClr)
# # pygame.display.update()
pygame.time.delay(2000)
hb=50
wb=50
xb=100
yb=300

cx=350
cy=350
speed=2
ibox= rad*math.squrt

square=(xb,yb,wb,hb)
squareClr=colors.get("pink") #creates the object to draw
# screen.fill(redClr)
# pygame.display.update()
# pygame.time.delay(2000)
circleClr=colors.get("blue")
#if i want this to keep running create a loop
backgrnd=colors.get('limeGreen')
run=True
speed=2
cx=350
cy=350
rad=25
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print('You quit')
        #rect(screen, redClr,square) ->
    keys= pygame.key.get_pressed() #this is a list
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x +=speed
    if keys [pygame.K_LEFT] and square.x > speed:
        square.x -= speed
    if keys[pygame.K_UP] and square.y >speed:
        square.y -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:
        square.y +=speed
    #move circle
    if keys[pygame.K_d] and cx <WIDTH -(rad):
        cx+= speed 
        insSquare.x += speed
    if keys[pygame.K_a] and cx >(speed+rad):
        cx += speed
        insSquare.x += speed
    if keys [pygame.K_w] and cy >(speed+rad):
        cy -= speed
        insSquare.y +=speed
    if keys [pygame.K_s] and cy <HEIGHT-(rad):
        cy += speed
        insSquare.y +=speed
    if square.colliderect(insSquare):
        print("BOOM")
         rad +=1

        cx=random.randit(rad,WIDTH-rad)
        cy=random.randit(rad,HEIGHT-rad)
       
    ibox= rad*math.squrt(2)
    xig = cx-(ibox/2)
    yig =cy-(ibox/2)

    pygame.draw.rect(screen, squareClr,square)
    pygame.draw.circle(screen,circleClr, (cx,cy),rad)
    pygame.draw.rect(screen, squareClr, insSquare)
    pygame.display.update()