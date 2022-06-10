#Susie Fagelman
#6/9/2022
#We are learning pygame basic functions
#creating screens, clrs, shape
from operator import truediv
import pygame, time
pygame.init() #initialize the pygame package
WIDTH=700 #like a constant 
HEIGHT=700
#create display window with anyname you like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #set_mode is how big you want the thing
pygame.display.set_caption("My First Game") #changes the title of my window
greenClr=(0,255,0)
purpleClr=(125,0,125)
# screen.fill(greenClr)
# pygame.display.update()
# pygame.time.delay(2000)
redClr=(255,0,0) #only want red (rgb)
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb) #creates the object to draw
# screen.fill(redClr)
# pygame.display.update()
# pygame.time.delay(2000)

#if i want this to keep running create a loop
background =greenClr
run=True
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print('You quit')
        #rect(screen, redClr,square) ->

    pygame.draw.rect(screen, redClr,square)
    pygame.draw.circle(screen,purpleClr, (350,350),25)
    pygame.display.update()