import pygame
from sys import exit

pygame.init()

width = 1280
height = 960
white = [255, 255, 255]
title = "Tetris"
screen = pygame.display.set_mode([width, height])
screen_size = pygame.display.get_window_size()
box = [(width - 500) / 2, (height - 700) / 2, 500, 700]
setTitle = pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.draw.rect(screen, (255, 0, 0), box, 2, border_radius=1)

    clock.tick(40)
    pygame.display.update()
pygame.quit()