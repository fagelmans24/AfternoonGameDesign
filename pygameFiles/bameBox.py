#Susie Fagelman
#06/17/22
#get username in pygame
import pygame, sys, os
pygame.init()
os.system('cls')
backgrndClr=(255,255,255)
clock=pygame.time.Clock
WIDTH=600
HEIGHT=600
screen=pygame.display. set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgrndClr)

run=True #run the while loop
user_name=''
nameClr=(0,125,125) #text for the name
bxClr= (200,200,200) #text b   

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//40)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

title=TITLE_FONT.render("enter Name" ,1, bxClr)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
screen.blit(title,(200,50))
Bx=WIDTH//3
Button_namebox= pygame.Rect(WIDTH//3, HEIGHT//3, WIDTH//4,40)
input_Rect= pygame.Rect(WIDTH//3, HEIGHT//3, 140, 32)

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # pygame.draw.rect(screen)
            #draw box
            print()
        if event.type==pygame.KEYDOWN:  
            if event.type==pygame.K_RETURN:
                print("Hello," + user_name)
            if event.key==pygame.K_BACKSPACE:
                user_name=user_name[:-1]
            else:
                user_name+= event.unicode
        pygame.draw.rect(screen, bxClr, input_Rect)

        text_surface=MENU_FONT.render(user_name, True, nameClr)
        #use your rectangle x and y to know where to put text 
        screen.blit(text_surface, (input_Rect.x+5, input_Rect.y+5))
        pygame.display.flip()

        # clock.tick(60) #run every second