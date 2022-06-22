
import pygame 
import time
pygame.init()

pygame.display.set_caption("Crossy Road")
#IMAGES
WIDTH = 500
HEIGHT = 480
background = pygame.image.load('pygameFiles\images\Pygame Crossy Road\\road background.jpg')
background = pygame.transform.scale (background, (WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT))      
clock = pygame.time.Clock()

def GameWindow():
    screen.blit(background, (0,0))
    
    pygame.display.update()
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    GameWindow()

pygame.quit()
