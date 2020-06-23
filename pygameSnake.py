#make it so that you cant move in the oppsite direction, if going left cant go right etv
import pygame
import random
#import time
#initializes pygame modules
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#creates a surface/the default surface where things appear
width = 800
height = 600
dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")

blockSize = 20
game_over = False

drawLines = True
#creates a clock object
clock = pygame.time.Clock()
snakeSpeed = 10
#makes a font object from the system fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35, bold = True)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])

def message(msg,color):
    #render creates a surface with text on it
    mesg = font_style.render(msg, True, color)
    #blit draws a source surface on THIS surface, takes source and destination
    dis.blit(mesg, [width/2, height/2])
def gameLoop():
    game_over = False
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    foodx = round(random.randrange(0, width - blockSize) /blockSize ) * blockSize
    foody = round(random.randrange(0, height - blockSize) /blockSize ) * blockSize
    direction = None
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    #this would be the size of the block
                    x1_change = -blockSize
                    y1_change = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    x1_change = blockSize
                    y1_change = 0
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'up':
                    y1_change = -blockSize
                    x1_change = 0
                    direction = 'down'
                elif event.key == pygame.K_DOWN and direction != 'down':
                    y1_change = blockSize
                    x1_change = 0
                    direction = 'up'
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        if drawLines:
            for i in range(0,height):
                if i % blockSize == 0:
                    pygame.draw.line(dis, black, (0, i), (width, i), 1)
            for i in range(0, width):
                if i % blockSize == 0:
                    pygame.draw.line(dis, black, (i, 0), (i, height), 1)
        pygame.draw.rect(dis, green, [foodx, foody, blockSize, blockSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                print("collide")
                game_over= True

        our_snake(blockSize, snake_list)


        your_score(snake_length - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - blockSize) /blockSize ) * blockSize
            foody = round(random.randrange(0, height - blockSize) /blockSize ) * blockSize
            snake_length += 1
            print("Yummy!!")

        clock.tick(snakeSpeed)
#updates screen, only updates par that are passed, no par = entire screen
    pygame.quit()
    quit()
gameLoop()
