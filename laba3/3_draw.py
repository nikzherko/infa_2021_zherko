import pygame
from pygame.draw import *

pygame.init()

red = (255, 0, 0)
green = (0, 204, 0)
black = (0, 0, 0)
FPS = 30
screen = pygame.display.set_mode((600, 600))

circle(screen, (255, 255, 0), (300, 300), 200, width=0)

polygon(screen, red, [[88, 88], [247, 183], [239, 197], [82, 102]])
polygon(screen, red, [[494, 119], [337, 194], [341, 207], [500, 133]])
circle(screen, green, (214, 260), 50)
circle(screen, green, (347, 260), 50)
circle(screen, black, (210, 242), 20)
circle(screen, black, (349, 251), 20)
rect(screen, black, (187, 369, 210, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()