#make it so that you cant move in the oppsite direction, if going left cant go right etv
import pygame
import random
from snake import Snake
#import time
#init
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

class snakeGame(object):
    def __init__(self):
        #creates a surface/the default surface where things appear
        pygame.init()
        self.width = 800
        self.height = 600
        self.xdim = 40
        self.ydim = 30
        self.dis = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("snake")

        self.blockSize = self.width / self.xdim
        self.game_over = False

        self.drawLines = True
        #creates a clock object
        self.clock = pygame.time.Clock()
        self.snakeSpeed = 10
        self.snake = Snake((self.xdim//2, self.ydim//2))
        #makes a font object from the system fonts
        self.font_style = pygame.font.SysFont(None, 50)
        self.score_font = pygame.font.SysFont("comicsansms", 35, bold = True)
    
    def our_snake(self, snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, black, [x[0], x[1], snake_block, snake_block])
     

    def your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, green)
        self.dis.blit(value, [0, 0])

    def message(self, msg, color):
        #render creates a surface with text on it
        mesg = self.font_style.render(msg, True, color)
        #blit draws a source surface on THIS surface, takes source and destination
        self.dis.blit(mesg, [ self.width/2,  self.height/2])

    def gameLoop(self):
        self.game_over = False
        # x1 = self.width / 2
        # y1 = self.height / 2

        # x1_change = 0
        # y1_change = 0
        # snake_list = []
        # snake_length = 1
        foodx = round(random.randrange(0, self.width - self.blockSize) /self.blockSize ) * self.blockSize
        foody = round(random.randrange(0, self.height - self.blockSize) /self.blockSize ) * self.blockSize
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        snake.setDirection((-1,0))
                        #this would be the size of the block
                        # x1_change = -self.blockSize
                        # y1_change = 0
                        # direction = 'left'
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        snake.setDirection((1,0))
                        # x1_change = self.blockSize
                        # y1_change = 0
                        # direction = 'right'
                    elif event.key == pygame.K_UP and self.direction != (0, 1):
                        snake.setDirection((0, -1))
                        # y1_change = -self.blockSize
                        # x1_change = 0
                        # direction = 'down'
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        snake.setDirection((0, 1))
                        # y1_change = self.blockSize
                        # x1_change = 0
                        # direction = 'up'
            if snake.direction[0] >= self.width or snake.direction[0] < 0 \
                    or snake.direction[1] >= self.height or snake.direction[1] < 0:
                self.game_over = True
            # x1 += x1_change
            # y1 += y1_change

            self.dis.fill(white)
            if self.drawLines:
                for i in range(0,self.height):
                    if i % self.blockSize == 0:
                        pygame.draw.line(self.dis, black, (0, i), (self.width, i), 1)
                for i in range(0, self.width):
                    if i % self.blockSize == 0:
                        pygame.draw.line(self.dis, black, (i, 0), (i, self.height), 1)

            pygame.draw.rect(self.dis, green, [foodx, foody, self.blockSize, self.blockSize])
            # snake_Head = []
            # snake_Head.append(x1)
            # snake_Head.append(y1)
            # snake_list.append(snake_Head)
            #adds the snake head to the end of the list,
            snake.move((foodx, foody))

            # if len(snake_list) > snake_length:
                # del snake_list[0]

            # for x in snake_list[:-1]:
                # if x == snake_Head:
                    # print("collide")
                    # self.game_over= True

            self.our_snake(self.blockSize, snake_list)


            self.your_score(snake_length - 1)
            pygame.display.update()
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.width - self.blockSize) /self.blockSize ) * self.blockSize
                foody = round(random.randrange(0, self.height - self.blockSize) /self.blockSize ) * self.blockSize
                snake_length += 1
                print("Yummy!!")

            self.clock.tick(self.snakeSpeed)
#updates screen, only updates par that are passed, no par = entire screen
        pygame.quit()
        quit()
if __name__ == "__main__":
    g = snakeGame()
    g.gameLoop()
