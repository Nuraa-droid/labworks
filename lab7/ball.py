import pygame

pygame.init()

w, h = 600, 600
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Game")

x, y = w//2, h//2
radius = 25
color = (255, 0, 0)
step = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - step >= 0:
                y -= step
            elif event.key == pygame.K_DOWN and y + radius + step <= h:
                y += step
            elif event.key == pygame.K_RIGHT and x + radius + step <= w:
                x += step
            elif event.key == pygame.K_LEFT and x - radius - step >= 0:
                x -= step

pygame.quit()



