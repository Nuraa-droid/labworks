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
COINS_TO_INCREASE_SPEED = 10

font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("AnimatedStreet.png")
 
screen = pygame.display.set_mode((400, 600))
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

# coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40)) # resize coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 100))
        self.value = random.choice([1, 2, 3])

    def move(self):
        global COINS, SPEED
        if pygame.sprite.collide_rect(self, P1): # check if playes collects coin
            COINS += self.value
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
            if COINS % COINS_TO_INCREASE_SPEED == 0:
                increase_enemy_speed()

# function to increase enemy speed     
def increase_enemy_speed():
    global SPEED
    SPEED += 1

# creating objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
 
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
            
# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    
    # check for collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over_screen()
        pygame.quit()
        sys.exit()
    
    # moving objects
    P1.move()
    E1.move()
    C1.move()
    
    background_y = 0
    # scrool background
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # sprites on screen
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    # score and coins on screen
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (300, 10))
    
    pygame.display.update()
    pygame.time.Clock().tick(60)
