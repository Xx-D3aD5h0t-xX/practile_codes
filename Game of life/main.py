import pygame as p
import sys
import time as t


# window vars
screenX = 1000
screenY = 750
bgR = 0
bgG = 0
bgB = 0

# pygame init
p.init()
clock = p.time.Clock()
root = p.display.set_mode((screenX+100, screenY))
favicon = p.image.load(r'Game of life\favicon.png').convert()
p.display.set_icon(favicon)
p.display.set_caption('Game Of Life')
p.font.init()
font = p.font.Font(r'.\Game of life\font.ttf', 24)
font30 = p.font.Font(r'.\Game of life\font.ttf', 30)


# main vars
side = 5
gridBool = False
resetBool = False
startCycle = False
l = []
gen = 0


# imgs
pause = p.image.load(r'Game of life\pause.png').convert()
play = p.image.load(r'Game of life\play.png').convert()
reset = p.image.load(r'Game of life\reset.png').convert()
resetInvert = p.image.load(r'Game of life\reset_invert.png').convert()
gridOff = p.image.load(r'Game of life\grid_off.png').convert()
gridOn = p.image.load(r'Game of life\grid_on.png').convert()


# functions
def createList():
    ls = []
    sl = []
    for i in range(0, (screenY)//side):
        for j in range(0, (screenX)//side):
            sl.append(0)
        ls.append(sl)
        sl = []
    return ls


# list creation

l = createList()


# -------------------------------------mainloop----------------------------
loop = True
while loop:

    fl = createList()


# events
    for event in p.event.get():
        # QUIT FUNCTION
        if event.type == p.QUIT:
            loop = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                if startCycle == False:
                    startCycle = True
                else:
                    startCycle = False
            if event.key == p.K_r:
                l = createList()
                gen = 0
                startCycle = False
                resetBool = True

            if event.key == p.K_g:
                if gridBool:
                    gridBool = False
                else:
                    gridBool = True

        if event.type == p.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = p.mouse.get_pos()
                if not mx >= 1000:
                    l[my//side][mx//side] = 1
                else:
                    pass

            if event.button == 3:
                mx, my = p.mouse.get_pos()
                l[my//side][mx//side] = 0

    root.fill((bgR, bgG, bgB))

# main code

    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            if l[i][j] == 0:
                col = (0, 0, 0)
            else:
                col = (255, 255, 255)
            p.draw.rect(root, col, p.Rect(j*side, i*side, side, side))

    # the main cycle
    if startCycle:
        minl = 0

        maxlx = len(l) - 1
        maxly = len(l[0]) - 1
        for i in range(0, len(l)):
            for j in range(0, len(l[i])):

                # checks
                # c1
                if i-1 < minl or j-1 < minl:
                    c1 = 0
                else:
                    c1 = l[i-1][j-1]

                # c2
                if i-0 < minl:
                    c2 = 0
                else:
                    c2 = l[i-1][j]

                # c3
                if i-1 < minl or j + 1 > maxly:
                    c3 = 0
                else:
                    c3 = l[i-1][j+1]

                # c4
                if j-1 < minl:
                    c4 = 0
                else:
                    c4 = l[i][j-1]

                # c5
                if j+1 > maxly:
                    c5 = 0
                else:
                    c5 = l[i][j+1]

                # c6
                if i+1 > maxlx or j-1 < minl:
                    c6 = 0
                else:
                    c6 = l[i+1][j-1]

                # c7
                if i + 1 > maxlx:
                    c7 = 0
                else:
                    c7 = l[i+1][j]

                # c8
                if i + 1 > maxlx or j + 1 > maxly:
                    c8 = 0
                else:
                    c8 = l[i+1][j+1]

                if l[i][j] == 0:
                    if c1+c2+c3+c4+c5+c6+c7+c8 == 3:
                        fl[i][j] = 1
                    else:
                        fl[i][j] = 0

                if l[i][j] == 1:
                    if c1+c2+c3+c4+c5+c6+c7+c8 == 2 or c1+c2+c3+c4+c5+c6+c7+c8 == 3:
                        fl[i][j] = 1
                    else:
                        fl[i][j] = 0

        l = fl
        gen += 1
    else:
        pass

    # lines and grid

    for i in range(0, screenX, side):
        if gridBool:
            p.draw.line(root, (90, 90, 90), (i, 0), (i, screenY), 1)
        else:
            pass
    for i in range(0, screenY, side):
        if gridBool:
            p.draw.line(root, (90, 90, 90), (0, i), (screenX, i), 1)
        else:
            pass

    p.draw.line(root, (255, 255, 255), (1005, 0), (1005, 750), 5)

    # img blit

    if startCycle:
        root.blit(play, (1020, screenY/2))
    else:
        root.blit(pause, (1020, screenY/2))

    if gridBool:
        root.blit(gridOn, (1020, 520))
    else:
        root.blit(gridOff, (1020, 520))

    if not resetBool:
        root.blit(reset, (1020, 240))
    else:
        root.blit(resetInvert, (1020, 240))
        resetBool = False

    # Text Blit
    startFont = font.render('Space', False, (255, 255, 255))
    root.blit(startFont, (1023, (screenY/2)+74))
    gridFont = font.render('G', False, (255, 255, 255))
    root.blit(gridFont, (1047, 520+74))
    resetFont = font.render('R', False, (255, 255, 255))
    root.blit(resetFont, (1047, 240+74))

    # gen text
    genText = font30.render('Gen:', False, (255, 255, 255))
    genNo = font30.render(str(gen), False, (255, 255, 255))
    root.blit(genText, (1023, 660))
    root.blit(genNo, (1023, 690))

    # gof text
    root.blit(font30.render('GAME', False, (255, 255, 255)), (1023, 30))
    root.blit(font30.render('OF', False, (255, 255, 255)), (1040, 60))
    root.blit(font30.render('LIFE', False, (255, 255, 255)), (1023, 90))

    # END
    clock.tick(60)
    p.display.flip()
