import sys
import pygame
import random

pygame.init()

n = 4

size = 100 * n
x = [50 + 100 * i for i in range(n)]

screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('I want more than 5, please')

tab = [[0 for i in range(n)] for i in range(n)]

flipp = True

def new(tab, n):
    a = []
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 0:
                a.append([i, j])
    m = int(random.uniform(0, len(a)))
    tab[a[m][0]][a[m][1]] = 2
    return tab

def add(a,n):
    s = [0 for j in range(n)]
    k = 0
    for j in range(n):
        if a[j] != 0:
            if s[k] == a[j]:
                s[k] = 2 * s[k]
                k += 1
            elif s[k] == 0:
                s[k] = a[j]
            else:
                k += 1
                s[k] = a[j]
    return s

while True:

    if flipp:

        tab = new(tab, n)

        screen.fill((0, 0, 0))

        for i in range(n):
            for j in range(n):
                myfont = pygame.font.SysFont("monospace", 40)
                label = myfont.render(str(tab[i][j]), 10, (255, 255, 255))
                screen.blit(label, (x[j], x[i]))

        pygame.display.flip()
        pygame.time.delay(250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            flipp = True
            for i in range(n):
                a = [tab[n - 1 - j][i] for j in range(n)]
                a = add(a, n)
                for j in range(n):
                    tab[j][i] = a[n - 1 - j]
        elif pygame.key.get_pressed()[pygame.K_UP]:
            flipp = True
            for i in range(n):
                a = [tab[j][i] for j in range(n)]
                a = add(a, n)
                for j in range(n):
                    tab[j][i] = a[j]
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            flipp = True
            for i in range(n):
                tab[i] = add(tab[i], n)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            flipp = True
            for i in range(n):
                a = [tab[i][n - 1 - j] for j in range(n)]
                a = add(a, n)
                tab[i] = [a[n - 1 - j] for j in range(n)]


        else:
            flipp = False
