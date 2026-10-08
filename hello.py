import pygame
import sys
from random import randint
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

# 1. Variables to hold the ball's position
gravity = 0.2
ball_x = 400
ball_x1 = 200
ball_y = 300
ball_y1 = 150
ball_radius = 20
speed_x = 2
speed_y = 5 + gravity
speed_x1 = 2
speed_y1 = 5 + gravity
bg_color = (0,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_x = ball_x + speed_x
    ball_y = ball_y + speed_y
    if ball_x > 800:
        speed_x = speed_x * -1
        bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
        speed_x = -randint(1,10)
        speed_y = -randint(1,10)
    if ball_y > 600:
        speed_y = speed_y * -1
        bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
        speed_x = -randint(1,10)
        speed_y = -randint(1,10)
    if ball_x < 0:
        speed_x = speed_x * -1
        bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
        speed_x = randint(1,10)
        speed_y = randint(1,10)
    if ball_y < 0:
        speed_y = speed_y * -1
        bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
        speed_x = randint(1,10)
        speed_y = randint(1,10)
    ball_x1 = ball_x1 + speed_x1
    ball_y1 = ball_y1 + speed_y1
    if ball_x1 > 800:
            speed_x1 = speed_x1 * -1
            bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
            speed_x1 = -randint(1,10)
            speed_y1 = -randint(1,10)
    if ball_y1 > 600:
            speed_y1 = speed_y1 * -1
            bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
            speed_x1 = -randint(1,10)
            speed_y1 = -randint(1,10)
    if ball_x1< 0:
            speed_x1 = speed_x1 * -1
            bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
            speed_x1 = randint(1,10)
            speed_y1 = randint(1,10)
    if ball_y1 < 0:
            speed_y1 = speed_y1 * -1
            bg_color = ((randint(0, 255), randint(0,255), randint(0,255)))
            speed_x1 = randint(1,10)
            speed_y1 = randint(1,10)
    screen.fill(bg_color)

    # 2. The single command to draw the ball
    pygame.draw.circle(screen, (100, 255, 100), (ball_x, ball_y), ball_radius)
    pygame.draw.circle(screen, (100, 255, 100), (ball_x1, ball_y1), ball_radius)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
