import pygame
import time
import math

def get_image(path, scale=None, size=None):
    image = pygame.image.load(path).convert_alpha()
    if size:
        return pygame.transform.scale(image, size)
    elif scale:
        new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
        return pygame.transform.scale(image, new_size)
    return image

pygame.init()

width, height = 700, 525
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

background = get_image("clock.png", size=(width, height))
left_hand = get_image("lhand.png", 0.5)
right_hand = get_image("rhand.png", 0.5)

center_x, center_y = width // 2, height // 2

running = True
while running:

    cur_time = time.localtime()
    minutes = cur_time.tm_min
    seconds = cur_time.tm_sec
    angle_min =  -(minutes * 6) + 300
    angle_sec =  - (seconds * 6) + 60


    rotated_right = pygame.transform.rotate(right_hand, angle_min)
    rotated_left = pygame.transform.rotate(left_hand, angle_sec)

    right_rect = rotated_right.get_rect(center=(center_x, center_y))
    left_rect = rotated_left.get_rect(center=(center_x, center_y))
    
    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(background, (width, height)), (0, 0))
    screen.blit(rotated_right, right_rect.topleft)
    screen.blit(rotated_left, left_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
