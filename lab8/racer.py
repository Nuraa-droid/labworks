import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("AnimatedStreet.png")
 
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")
 
 
# enemy car
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() # area of image
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) # random start position
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED) # move enemy downward
        if (self.rect.top > 600): # if enemy goes off scxreen, reset position
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Flags for speed increase based on coin collection 
c1, c2, c3, c4, c5 = False, False, False, False, False
# coins
class Coin(pygame.sprite.Sprite):
    def spawn_near_player(self):
        while True:
            new_x = random.randint(40, SCREEN_WIDTH - 40)
            new_y = random.randint(100, SCREEN_HEIGHT - 100)
            if abs(new_x - P1.rect.x) > 50 and abs(new_y - P1.rect.y) > 50:
                self.rect.center = (new_x, new_y)
                break

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40)) # resize coin
        self.rect = self.image.get_rect()
        self.spawn_near_player()

    def move(self):
        global COINS, SPEED
        if pygame.sprite.collide_rect(self, P1): # check if playes collects coin
            if self.rect.bottom < SCREEN_HEIGHT // 3:
                COINS += 3
            elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
                COINS += 2
            else:
                COINS += 1
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        
        # increase speed based on collected coins
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True

# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # initial position of player
        
    def move(self):
        # moves based on key pressed
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 5:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH - 5:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(7, 0)
        if self.rect.top > 5:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -7)
        if self.rect.bottom < SCREEN_HEIGHT - 5:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 7)

# creating objects
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
# event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# game over
def game_over_screen():
    screen.fill(RED)
    text = font.render("Game Over", True, BLACK)
    scoret = font.render(f"Score: {SCORE}", True, BLACK)
    coinst = font.render(f"Coins: {COINS}", True, BLACK)
   
    screen.blit(text, (120, 200))
    screen.blit(scoret, (120, 250))
    screen.blit(coinst, (120, 300))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                return True
        
background_y = 0
 
# main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.1
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.sprite.spritecollideany(P1, enemies): # check for collision with enemy
        game_over_screen()
        pygame.quit()
        
    # scrool background
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))
    
    # display score and coins
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))
    
    P1.move()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        for enemy in enemies:
            enemy.move()
        for coin in coinss:
            coin.move()
   
    pygame.display.update()
    FramePerSec.tick(FPS)