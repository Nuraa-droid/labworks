import pygame
import math

# constants 
w, h = 1200, 800
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

# settings
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
screen.fill(white)

# variables
drawing = False 
color = black
mode = "brush" # brush, rect, circle, eraser
start_pos = None

# color selection panel
def draw():
    pygame.draw.rect(screen, red, (10, 10, 30, 30))
    pygame.draw.rect(screen, green, (50, 10, 30, 30))
    pygame.draw.rect(screen, blue, (90, 10, 30, 30))
    pygame.draw.rect(screen, black, (130, 10, 30, 30))
    pygame.draw.rect(screen, white, (170, 10, 30, 30))

draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user closes the window
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: # mouse button pressed
            x, y = event.pos # click coordinates
            if 10 <= x <= 40 and 10 <= y <= 40:
                color = red
            elif 50 <= x <= 80 and 10 <= y <= 40:
                color = green
            elif 90 <= x <= 120 and 10 <= y <= 40:
                color = blue
            elif 130 <= x <= 160 and 10 <= y <= 40:
                color = black
            elif 170 <= x <= 200 and 10 <= y <= 40:
                color = white
            else:
                drawing = True # start drawing
                start_pos = event.pos # ending position
        
        elif event.type == pygame.MOUSEBUTTONUP: # mouse button released
            drawing = False # stop drawing
            end_pos = event.pos
            if mode == "rect": # rect mode selected
                x1, y1 = start_pos
                x2, y2 = end_pos
                w1 = abs(x2 - x1) # calculating width
                h1 = abs(y2 - y1) # calculating height
                pygame.draw.rect(screen, color, (min(x1, x2), min(y1, y2), w1, h1), 2)

            elif mode == "circle": # circle mode selected
                x1, y1 = start_pos
                x2, y2 = end_pos
                r = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) # calculating radius
                pygame.draw.circle(screen, color, start_pos, r, 2)

        elif event.type == pygame.MOUSEMOTION: # mouse movement
                if drawing:
                    if mode == "brush": # brush mode is selected
                        pygame.draw.circle(screen, color, event.pos, 5) # draw with brush
                    elif mode == "eraser": # eraser mode is selected
                        pygame.draw.circle(screen, white, event.pos, 10) 
        # swith tools         
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # rectangle mode
                mode = "rect"
            elif event.key == pygame.K_c: # circle mode
                mode = "circle"
            elif event.key == pygame.K_b: # brush mode
                mode = "brush"
            elif event.key == pygame.K_e: # eraser mode
                mode = "eraser"
    pygame.display.flip() # update the screen 
pygame.quit() # quit pygame

