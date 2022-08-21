
import pygame


# window vars___________________________
screen_x = 600
screen_y = 600
bg_r = 30
bg_g = 210
bg_b = 10

# ball vars____________________________
r = 10
mass = 1
acc = mass*0.5
v = 0
ix = 300
iy = -300
b = 0
elastic = 0.9
time = pygame.time.get_ticks()
elasticity = 0
lowering_const = 0.4
lowering_const_sum = 0
bi = 0
bounce = 0
arb_i = 0


# Pygame init____________________
pygame.init()
clock = pygame.time.Clock()
root = pygame.display.set_mode((screen_x, screen_y+140))


# Mainloop________________________
loop = True
while loop:
    for event in pygame.event.get():
        # QUIT FUNCTION
        if event.type == pygame.QUIT:
            loop = False
    root.fill((bg_r, bg_g, bg_b))

    # ball
    v += acc
    ball = pygame.draw.circle(root, (255, 255, 255), (ix, iy), r)
    if iy >= 680:
        lowering_const_sum += lowering_const
        if lowering_const_sum >= bounce-elastic:
            lowering_const_sum = bounce-elastic
        bi += bounce - lowering_const_sum

        # dist calculation
        if arb_i == 0:
            time = (pygame.time.get_ticks())/1000
            elasticity = v*time
            bounce = elasticity/6.9
            print(elasticity)
            time = 0
            arb_i += 1

        # elastic thingy
        if bi >= elastic*elasticity:
            bi = elastic*elasticity

        v = 0
        b = (elastic*elasticity) - bi
        if b <= 0:
            b = 0

    iy += v
    iy -= b
    if b <= 0:
        b = 0

    else:
        b -= 0.1

    clock.tick(60)
    pygame.display.flip()
