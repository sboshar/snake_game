import pygame
import sys
#initalizes the pygame
pygame.init()

win = pygame.display.set_mode((400,400))
pygame.display.set_caption("My First Pygame")

x = 50
y = 50
width = 40
height = 60
velocity = 10

run = True
while run:
    #adds a delay so that the object moves more slowly
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity
        if x == 0:
            print("game over")
            sys.exit()
    if keys[pygame.K_RIGHT]:
        x+=velocity
        if x == 360:
            print("game over")
            pygame.quit()
            sys.exit()
    if keys[pygame.K_UP]:
        y-=velocity
        if y == 0:
            print("game over")
            pygame.quit()
            sys.exit()
    if keys[pygame.K_DOWN]:
        y += velocity
        if y == 340:
            print("game over")
            pygame.quit()
            sys.exit()
    win.fill((0,0,0))

    pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    pygame.display.update()

pygame.quit()

