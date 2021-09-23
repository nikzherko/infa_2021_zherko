import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
FPS = 30
bezh = (225, 229, 204)
pink = (255, 51, 153)
red = (255, 0, 0)
blue = (102, 178, 255)
brown = (204, 102, 0)
green = (0, 153, 76)
black = (0, 0, 0)
purple = (102, 102, 255)

def body(cvet, centr_kruga_1, centr_kruga_2, radius):
    circle(screen, cvet, (centr_kruga_1, centr_kruga_2), radius)

def shoulder(cvet, pervaya, vtoraya, tri, chetiri):
    polygon(screen, cvet,
            [
                [pervaya, vtoraya],
                [pervaya, vtoraya - 50],
                [pervaya - 46, vtoraya - 64],
                [pervaya - 76, vtoraya - 28],
                [pervaya - 47, vtoraya + 14]
            ]
            )

    polygon(screen, cvet,
             [
                [tri, chetiri],
                [tri, chetiri - 50],
                [tri + 46, chetiri - 64],
                [tri + 74, chetiri - 28],
                [tri + 49, chetiri + 14]
             ]
            )

def hands(cvet, odin, dva, centr_1, centr_2, radius):
    polygon(screen, cvet,
            [
                [odin, dva],
                [odin - 53, dva - 290],
                [odin - 34, dva - 293],
                [odin + 18, dva]
            ]
            )
    polygon(screen, cvet,
            [
                [odin + 289, dva - 7],
                [odin + 338, dva - 301],
                [odin + 355, dva - 290],
                [odin + 309, dva - 3]
            ]
            )
    circle(screen, cvet, (centr_1, centr_2), radius)
    circle(screen, cvet, (centr_1 + 380, centr_2), radius)

def head(cvet, centr_1, centr_2, radius):
    circle(screen, cvet, (centr_1, centr_2), radius)

def eyes(cvet_1, cvet_2,  c_1, c_2, radius):
    circle(screen, cvet_1, (c_1, c_2), radius)
    circle(screen, cvet_1, (c_1 + 92, c_2), radius)

    circle(screen, cvet_2, (c_1, c_2), radius - 20)
    circle(screen, cvet_2, (c_1 + 92, c_2), radius - 20)

def nose(cvet, tochka):
    polygon(screen, cvet, [[tochka, tochka + 103], [tochka + 35, tochka + 103], [tochka + 18, tochka + 130]])

def mouth(cvet, tochka):
    polygon(screen, cvet, [[tochka, tochka + 197], [tochka + 130, tochka + 197], [tochka + 65, tochka + 229]])

def plakat(cvet, tochka):
    rect(screen, cvet, (tochka, tochka + 40, tochka + 430, tochka + 30))

def nadpis(tekst, tochka):
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = myfont.render(tekst, False, (0, 0, 0))
    screen.blit(textsurface, (tochka, tochka + 25))

def hair(cvet, odin, dva):
    polygon(screen, cvet,
            [
                [odin, dva],
                [odin + 12, dva - 51],
                [odin + 46, dva - 13]
            ]
            )

    polygon(screen, cvet,
            [
                [odin + 40, dva - 11],
                [odin + 60, dva - 49],
                [odin + 88, dva - 15]
            ]
            )

    polygon(screen, cvet,
            [
                [odin + 80, dva - 14],
                [odin + 115, dva - 52],
                [odin + 127, dva + 4]
            ]
            )

body(pink, 295, 600, 150)
shoulder(pink, 195, 516, 398, 516)
hands(bezh, 142, 465, 100, 170, 30)
head(bezh, 290, 370, 120)
eyes(blue, black, 236, 330, 30)
nose(brown, 267)
mouth(red, 219)
hair(green, 233, 269)
plakat(green, 50)
nadpis('PYTHON IS AMAZING', 65)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()