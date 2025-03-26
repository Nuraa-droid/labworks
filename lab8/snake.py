import pygame
import random

pygame.init()

# размеры окна
w, h = 600, 400
cell = 10

# colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# инициализация змеи
snake = [(100, 100), (80, 100), (60, 100)]
direction = (cell, 0)
speed = 5

# создание окна
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")

# шрифт
font = pygame.font.Font(None, 36)

# функция для рисования стены
def draw_walls():
    for x in range(0, w, cell): # перебираем координаты по оси х с шагом cell
        pygame.draw.rect(screen, blue, (x, 0, cell, cell)) # верхняя граница
        pygame.draw.rect(screen, blue, (x, h - cell, cell, cell)) # нижняя граница
    for y in range (0, h, cell): # перебираем координаты по оси у с шагом cell
        pygame.draw.rect(screen, blue, (0, y, cell, cell)) # левая граница
        pygame.draw.rect(screen, blue, (w - cell, y, cell, cell)) # правая граница

# функция для генерации еды
def generate_food(snake):
    while True:
        food = random.randint(1, (w // cell) - 2) * cell, random.randint(1, (h // cell) - 2) * cell
        if food not in snake:
            return food
        
# инициализация еды
food = generate_food(snake)

# score and level
score = 0
level = 1

# цикл игры
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(black)
    draw_walls()
    pygame.draw.rect(screen, red, (food[0], food[1], cell, cell))

    #отработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell):
                direction = (0, -cell)
            elif event.key == pygame.K_DOWN and direction != (0, -cell):
                direction = (0, cell)
            elif event.key == pygame.K_LEFT and direction != (cell, 0):
                direction = (-cell, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell, 0):
                direction = (cell, 0)
   
    # движение змеи
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    # проверка на столкновение со стенами
    if new_head[0] <= 0 or new_head[0] >= w - cell or new_head[1] <= 0 or new_head[1] >= h - cell:
        running = False  # Заканчиваем игру при выходе за границы
    if new_head in snake:
        running = False  # Заканчиваем игру при столкновении с собой
    # добавление новой головы 
    snake.insert(0, new_head)

    #проверка еды
    if new_head == food:
        food = generate_food(snake)
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
            snake.pop()

    # отрисовка змеи
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell, cell))

    # отображение счета и уровня
    scoret = font.render(f"Score: {score}", True, white)
    levelt = font.render(f"Level: {level}", True, white)
    screen.blit(scoret, (10, 10))
    screen.blit(levelt, (10, 40))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

