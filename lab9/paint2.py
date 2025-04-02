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

font = pygame.font.SysFont(None, 20)
text_lines = [
    "brush - b",
    "rectangle - r",
    "circle - c",
    "eraser - e",
    "square - s",
    "right triangle - t",
    "equilateral triangle - y",
    "rhombus - h"
]
y = 20
for line in text_lines:
    text_surface = font.render(line, True, black)
    screen.blit(text_surface, (1050, y))
    y += 15
pygame.display.flip()

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
            if start_pos is not None:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
            w1 = abs(x2 - x1) # calculating width
            h1 = abs(y2 - y1) # calculating height
            if mode == "rect": # rect mode selected
                pygame.draw.rect(screen, color, (min(x1, x2), min(y1, y2), w1, h1), 2)

            elif mode == "circle": # circle mode selected
                center_x = (x1 + x2) // 2
                center_y = (x1 + x2) // 2
                r = max(w1, h1) // 2
                pygame.draw.circle(screen, color, (center_x, center_x), r, 2)

            elif mode == "square": # square mode selected
                side = min(w1, h1)
                pygame.draw.rect(screen, color, (min(x1, x2), min(y1, y2), side, side), 2)
            
            elif mode == "right triangle": # right triangle mode selected
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, color, points, 2)

            elif mode == "equilateral triangle": # equilateral triangle mode selected
                side_length = min(w1, h1)
                top = (x1 + side_length // 2, y1)
                left = (x1, y1 + int(math.sqrt(3) / 2 * side_length))
                right = (x1 + side_length, y1 + int(math.sqrt(3) / 2 * side_length))
                pygame.draw.polygon(screen, color, [top, left, right], 2)

            elif mode == "rhombus": # rhombus mode selected
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2 
                height = h1
                width = w1
                top = (center_x, center_y - height // 2)
                bottom = (center_x, center_y + height // 2)
                left = (center_x - width // 2, center_y)
                right = (center_x + width// 2, center_y)
                pygame.draw.polygon(screen, color, [top, right, bottom, left], 2)
        
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
            elif event.key == pygame.K_t: # r triangle mode
                mode = "right triangle"
            elif event.key == pygame.K_y:
                mode = "equilateral triangle" # e triangle mode
            elif event.key == pygame.K_h: # rhomdus mode
                mode = "rhombus"
            elif event.key == pygame.K_s: # square mode
                mode = "square"

    pygame.display.update() # update the screen 
pygame.quit() # quit pygame

