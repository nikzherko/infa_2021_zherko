import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
FPS = 30
bezh = (225, 229, 204)
pink = (255, 51, 153)
red = (255, 0, 0)
blue = (102, 178, 255)
brown = (204, 102, 0)
green = (0, 153, 76)
black = (0, 0, 0)
purple = (102, 102, 255)

def bodies(cvet_1, cvet_2, centr, radius):
    circle(screen, cvet_1, (centr, centr + 305), radius)
    circle(screen, cvet_2, (centr + 400, centr + 305), radius)

def heads(cvet, centr, radius):
    circle(screen, cvet, (centr, centr + 80), radius)
    circle(screen, cvet, (centr + 400, centr + 80), radius)

def eyes(cvet_glaz_1, cvet_glaz_2,  cvet_zrachkov,  centr, radius):
    circle(screen, cvet_glaz_1, (centr, centr + 94), radius)
    circle(screen, cvet_glaz_1, (centr + 92, centr + 94), radius)
    circle(screen, cvet_glaz_2, (centr + 400, centr + 94), radius)
    circle(screen, cvet_glaz_2, (centr + 492, centr + 94), radius)
    circle(screen, cvet_zrachkov, (centr, centr + 94), radius - 20)
    circle(screen, cvet_zrachkov, (centr + 92, centr + 94), radius - 20)
    circle(screen, cvet_zrachkov, (centr + 400, centr + 94), radius - 20)
    circle(screen, cvet_zrachkov, (centr + 492, centr + 94), radius - 20)

def noses(cvet, nachalo):
    polygon(screen, cvet,
    [
        [nachalo, nachalo + 103],
        [nachalo + 35, nachalo + 103],
        [nachalo + 18, nachalo + 130]
    ]
            )
    polygon(screen, cvet,
    [
        [nachalo + 400, nachalo + 103],
        [nachalo + 435, nachalo + 103],
        [nachalo + 418, nachalo + 130]
    ]
            )

def mouth(cvet, nachalo):
    polygon(screen, cvet,
            [
                [nachalo, nachalo + 197],
                [nachalo + 150, nachalo + 197],
                [nachalo + 65, nachalo + 229]
            ]
            )
    polygon(screen, cvet,
            [
                [nachalo + 400, nachalo + 197],
                [nachalo + 530, nachalo + 197],
                [nachalo + 465, nachalo + 229]
            ]
            )

def hands(cvet, nachalo):
    polygon(screen, cvet,
            [
                [nachalo, nachalo + 323],
                [nachalo - 53, nachalo + 33],
                [nachalo - 34, nachalo + 30],
                [nachalo + 18, nachalo + 322]
            ]
            )
    polygon(screen, cvet,
            [
                [nachalo + 289, nachalo + 316],
                [nachalo + 338, nachalo + 22],
                [nachalo + 355, nachalo + 33],
                [nachalo + 309, nachalo + 320]
            ]
            )
    polygon(screen, cvet,
            [
                [nachalo + 400, nachalo + 323],
                [nachalo + 347, nachalo + 33],
                [nachalo + 366, nachalo + 30],
                [nachalo + 418, nachalo + 322]
            ]
            )
    polygon(screen, cvet,
            [
                [nachalo + 689, nachalo + 316],
                [nachalo + 738, nachalo + 22],
                [nachalo + 755, nachalo + 33],
                [nachalo + 709, nachalo + 320]
            ]
            )

def shoulders(cvet_1, cvet_2, nachalo):
    polygon(screen, cvet_1,
            [
                [nachalo, nachalo + 320],
                [nachalo, nachalo + 271],
                [nachalo - 47, nachalo + 256],
                [nachalo - 77, nachalo + 291],
                [nachalo - 48, nachalo + 334]
            ]
            )
    polygon(screen, cvet_2,
            [
                [nachalo + 399, nachalo + 320],
                [nachalo + 400, nachalo + 271],
                [nachalo + 353, nachalo + 256],
                [nachalo + 323, nachalo + 292],
                [nachalo + 353, nachalo + 335]
            ]
            )
    polygon(screen, cvet_1,
            [
                [nachalo + 203, nachalo + 321],
                [nachalo + 203, nachalo + 271],
                [nachalo + 249, nachalo + 256],
                [nachalo + 277, nachalo + 293],
                [nachalo + 252, nachalo + 334]
            ]
            )
    polygon(screen, cvet_2,
            [
                [nachalo + 603, nachalo + 321],
                [nachalo + 603, nachalo + 271],
                [nachalo + 649, nachalo + 256],
                [nachalo + 677, nachalo + 293],
                [nachalo + 652, nachalo + 334]
            ]
            )

def kist(cvet, centr, radius):
    circle(screen, cvet, (centr, centr + 70), radius)
    circle(screen, cvet, (centr + 380, centr + 70), radius)
    circle(screen, cvet, (centr + 400, centr + 70), radius)
    circle(screen, cvet, (centr + 780, centr + 70), radius)

def tablichka(cvet, nachalo):
    rect(screen, cvet, (nachalo, nachalo + 40, nachalo + 830, nachalo + 30))

def nadpis(tekst, point):
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = myfont.render(tekst, False, (0, 0, 0))
    screen.blit(textsurface, (point, point - 90))

def hair(cvet_1, cvet_2, odin, dva):
    polygon(screen, cvet_1,
            [
                [odin, dva],
                [odin + 12, dva - 51],
                [odin + 46, dva - 13]
            ]
            )

    polygon(screen, cvet_1,
            [
                [odin + 40, dva - 11],
                [odin + 60, dva - 49],
                [odin + 88, dva - 15]
            ]
            )

    polygon(screen, cvet_1,
            [
                [odin + 80, dva - 14],
                [odin + 115, dva - 52],
                [odin + 127, dva + 4]
            ]
            )

    polygon(screen, cvet_2,
            [
                [odin + 400, dva],
                [odin + 412, dva - 51],
                [odin + 446, dva - 13]
            ]
            )

    polygon(screen, cvet_2,
            [
                [odin + 440, dva - 11],
                [odin + 460, dva - 49],
                [odin + 488, dva - 15]
            ]
            )

    polygon(screen, cvet_2,
            [
                [odin + 480, dva - 14],
                [odin + 515, dva - 52],
                [odin + 527, dva + 4]
            ]
            )

bodies(pink, purple, 295, 150)
heads(bezh, 290, 120)
eyes(green, blue, black, 236, 30)
noses(brown, 267)
mouth(red, 219)
hands(bezh, 142)
shoulders(pink, purple, 195)
kist(bezh, 100, 30)
tablichka(green, 50)
nadpis('PYTHON IS REALLY GOOD!!!!!!', 180)
hair(blue, green, 233, 269)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()