import pygame
import random

# 初始化游戏
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置游戏窗口尺寸
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("贪吃蛇小游戏")

# 定义蛇的初始位置和大小
snake_size = 20
snake_x = screen_width / 2
snake_y = screen_height / 2

# 定义蛇的移动速度
snake_speed = 10
snake_x_change = 0
snake_y_change = 0

# 定义食物的初始位置和大小
food_size = 20
food_x = round(random.randrange(0, screen_width - food_size) / 20.0) * 20.0
food_y = round(random.randrange(0, screen_height - food_size) / 20.0) * 20.0

# 定义得分
score = 0

# 游戏结束标志
game_over = False

# 游戏主循环
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    snake_x += snake_x_change
    snake_y += snake_y_change

    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    window.fill(BLACK)
    pygame.draw.rect(window, GREEN, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(window, BLUE, [snake_x, snake_y, snake_size, snake_size])

    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, screen_width - food_size) / 20.0) * 20.0
        food_y = round(random.randrange(0, screen_height - food_size) / 20.0) * 20.0

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
