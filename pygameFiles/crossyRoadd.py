#Susie Fagelman
#Crossy
import pygame 
import time
pygame.init()

# colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),}

# IMAGES
WIDTH = 500
HEIGHT = 480
pygame.init()
background = pygame.image.load(r'pygameFiles\\images\\Pygame Crossy Road\\road background.jpg')
background = pygame.transform.scale (background, (WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Crossy Road")     
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
        screen.fill ((0,255,0))
        duck_group.draw(screen)


    GameWindow()


def update (self):
        self. move()
        self. correction ()
        self.checkCollision()
        self.rect.center = (self.x, self.y)
def move(self):
    keys= pygame.key.get_pressed
    if keys[pygame.K_LEFT]:
        self.x -= self.vel  #changing x position by the velocity
        self. image = self. duckleft
    elif keys[pygame. K_RIGHT]:
        self.x += self.vel
        self.image = self.duckright
    if keys[pygame.K_UP]:
        self.y -= self.vel
    elif keys[pygame. K_DOWN]:
        self.y += self.vel
def correction(self):
    if self.x - self.width /2 < 0:
        self.x = self.width/2
    elif self.x +self.width /2 > WIDTH:
        self.x = WIDTH -self.width/2 
    if self.y - self.height /2 < 0:
        self.y = self.height/2
    elif self.y +self.height /2 > HEIGHT:
        self.x = HEIGHT -self.height/2
def checkCollision(self):
    car_check= pygame.sprite.spritecollide(self, car_group, False, pygame.sprite.collide_mask)
    if car_check:
        explosion.explode(self.x, self.y)
    
class duck(pygame.sprite.Sprite):
    def __init__ (self):
        super (). __init__ ()
        self.x = 50
        self.y = HEIGHT//2
        self.width = 100
        self.height = 50
        self.vel=4 #vel is the speed which the character moves #vel to speed

        #IMAGES
        self. duckright = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct duck1.png')
        self.duckleft  = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct duck2.png')
        self. duckright = pygame. transform. scale(self. duckright, (75,75))
        self. duckleft = pygame. transform. scale(self. duckleft, (75,75))

        self. image = self.duckright
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.correction()
        self.checkCollision()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.image = self.duckright

        elif keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.image = self.duckleft

        if keys[pygame.K_UP]:
            self.y -= self.vel

        elif keys[pygame.K_DOWN]:
            self.y += self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

    def checkCollision(self):
        car_check = pygame.sprite.spritecollide(self, car_group, False, pygame.sprite.collide_mask)
        if car_check:
            explosion.explode(self.x, self.y)

        #IMAGES #since characters are sprites they need an image 
        
class Car(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.x = 190
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct blue slow car.png')
            self.vel = -4

        else:
            self.x = 460
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\\red fast car.png')
            self.vel = 5

        self.y = HEIGHT / 2
        self.width = 100
        self.height = 150
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.y += self.vel

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1



class Screen(pygame.sprite.Sprite):
    def __init__ (self):
        super(). __init__()
        self. image1= pygame.image.load('pygameFiles\images\Pygame Crossy Road\\road background.jpg')
        self. image2= pygame.image.load('pygameFiles\images\Pygame Crossy Road\You Win.png')
        self. image3 = pygame.image.load('pygameFiles\images\Pygame Crossy Road\You lose.png')

        self.image1= pygame.transform.scale(self.image1, (WIDTH, HEIGHT))
        self.image2= pygame.transform.scale(self.image2, (WIDTH, HEIGHT))
        self.image3= pygame.transform.scale(self.image3, (WIDTH, HEIGHT))

        self.image = self.image1
        self.x = 0  #want background to start at top left of screen
        self.y = 0

        self.rect = self. image.get_rect() #getting rectangle to move sprite around 

    def update(self):
        self.rect.topleft = (self.x, self.y)

class Flag(pygame.sprite.Sprite):
    def __init__ (self, number):
        super().__init__() #look this up
        self.number = number

        if self.number ==1:
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\green flag.png')
            self.visible = False
            self.x = 50
        else:
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\white flag.png')
            self.visible = True
            self.x = 580 #opposite end of the screen 
       
        self.y = HEIGHT / 2
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.visible:
            self.collision()
            self.rect.center = (self.x, self.y)

    def collision(self):
        global SCORE, duck

        flag_hit = pygame.sprite.spritecollide(self, duck_group, False, pygame.sprite.collide_mask)
        if flag_hit:
            self.visible = False

            if self.number == 1:
                white_flag.visible = True
                if SCORE < 5:
                    SwitchLevel()

                else:
                    duck_group.empty()
                    DeleteOtherItems()

                    EndScreen(1)

            else:
                green_flag.visible = True

class Explosion(object):  
    def __init__(self)    :
        self.costume =1
        self.width =140
        self.height =140
        self.image =pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct boom image.png')  #explosion if series of images  
        self.image =pygame.transform.scale(self.image, (self.width, self.height))

    def explode(self, x,y): #x and y are ducks coordinates 
        #make sure explosions go to right place
        x =x-self.width//2
        y=y -self.height//2
        DeleteDuck() #calling the method

        while self.costume <9:
            self.image =pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct boom image.png')  #explosion if series of images  
            self.image =pygame.transform.scale(self.image, (self.width, self.height))
            screen.blit(self.image,(x,y))
            pygame.display.update()
            self.costume +=1
            time.sleep(0.1)

        DeleteOtherItems() #clears screen
        EndScreen(0) #after explosion, player has lost 

def ScoreDisplay():
    global gameOn
    if gameOn:
        score_text=score_font.render(str(SCORE) + ' / 5', True, (0,0,0))
        screen.blit(score_text, (255, 10)) #blitting score on x and y position 

def checkFlags():
    for flag in flags:
        if not flag.visible:
            flag.kill()

        else:
            if not flag.alive():
                flag_group.add(flag)
def SwitchLevel():
    global SCORE #making it global as we will change the score by 1 later 

    if slow_car.vel<0:
        slow_car.vel -= 1

    else:
        slow_car.vel +=1
    
    if fast_car.vel<0:
        fast_car.vel -= 1

    else:
        fast_car.vel +=1
    
    SCORE +=1

def DeleteDuck(): #removing duck from that group
    global Duck  
    Duck.kill()
    screen_group.draw(screen)
    car_group.draw(screen)
    flag_group.draw(screen)

    screen_group.update()
    car_group.update()
    flag_group.update()

    pygame.display.update()

def DeleteOtherItems():
    car_group.empty()
    flag_group.empty()
    flags.clear()

def EndScreen(number):
    global gameOn
    gameOn=False
    if number ==0:
        bg.image =bg.image3
        pygame.time.delay(3000)

    elif number==1:
        bg.image =bg.image2

def gameOver(num):
    screen.fill((255,255,255))
    if num==0:
        text= ('You lost the game, do you want to play again?')
    if num==1:
        text= ('You won the game, do you want to play again?')
    text=score_font.render(text, 1, (0,0,0))
    xd=  WIDTH//2-(text.get_width()//2)
    screen.blit(text,(xd, 50))
    

    
    
#VARIABLES

WIDTH = 640
HEIGHT= 480

pygame.init()
screen =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crossy Road')
clock = pygame.time.Clock()

SCORE=0
score_font = pygame.font.SysFont('comicsans', 80, True) 

bg = Screen()
screen_group = pygame.sprite.Group()    #for a sprite to work it needs a group
screen_group.add(bg)   #creating group

Duck = duck()
duck_group = pygame.sprite.Group()
duck_group.add(Duck)

slow_car =Car(1)
fast_car =Car(2)
car_group = pygame.sprite.Group()
car_group.add(slow_car, fast_car)

green_flag =Flag(1)
white_flag =Flag(2)
flag_group=pygame.sprite.Group()
flag_group.add(green_flag, white_flag)
flags = [green_flag, white_flag] #list with two objects
explosion =Explosion()

gameOn = True

run =True
while run: #main loop where we call all functions 

    GameWindow()
    clock.tick(60)  #setting up a framerate of 60 frames per second    for event in pygame.event.get():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen_group.draw(screen)
    ScoreDisplay()
    checkFlags()

    car_group.draw(screen)
    duck_group.draw(screen)
    flag_group.draw(screen)

    car_group.update()
    duck_group.update()
    flag_group.update()

    screen_group.update()

    pygame.display.update()

pygame.quit()


