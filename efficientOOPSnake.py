#make it so that you cant move in the oppsite direction, if going left cant go right etv
import pygame
import random
from snake import Snake
from board import Board
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
        self.num_rows = 30
        self.num_cols = 40

        self.board = Board(self.num_rows, self.num_cols)
        
        self.dis = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("snake")

        self.blockSize = self.width / self.num_cols 
        self.game_over = False

        self.drawLines = True
        #creates a clock object
        self.clock = pygame.time.Clock()
        self.snakeSpeed = 10
        self.snake = Snake((self.num_cols//2, self.num_rows//2))
        #makes a font object from the system fonts
        #self.font_style = pygame.font.SysFont(None, 50)
        #self.score_font = pygame.font.SysFont("comicsansms", 35, bold = True)
    
#     def our_snake(self, snake_block, snake_list):
        # for x in snake_list:
            # pygame.draw.rect(self.dis, black, [x[0], x[1], snake_block, snake_block])
     

    # def your_score(self, score):
        # value = self.score_font.render("Your Score: " + str(score), True, green)
        # self.dis.blit(value, [0, 0])

    # def message(self, msg, color):
        # #render creates a surface with text on it
        # mesg = self.font_style.render(msg, True, color)
        # #blit draws a source surface on THIS surface, takes source and destination
        # self.dis.blit(mesg, [ self.width/2,  self.height/2])

    def makeGrid(self):
        for i in range(0,self.height):
            if i % self.blockSize == 0:
                pygame.draw.line(self.dis, black, (0, i), (self.width, i), 1)
        for i in range(0, self.width):
            if i % self.blockSize == 0:
                pygame.draw.line(self.dis, black, (i, 0), (i, self.height), 1)


    def gameLoop(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.setDirection((-1,0))
                        #this would be the size of the block
                        # x1_change = -self.blockSize
                        # y1_change = 0
                        # direction = 'left'
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.setDirection((1,0))
                        # x1_change = self.blockSize
                        # y1_change = 0
                        # direction = 'right'
                    elif event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.setDirection((0, -1))
                        # y1_change = -self.blockSize
                        # x1_change = 0
                        # direction = 'down'
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.setDirection((0, 1))
                        # y1_change = self.blockSize
                        # x1_change = 0
            
                        # direction = 'up'

            self.dis.fill(white)
            if self.drawLines: self.makeGrid()
            # print(self.board.shape())
            # print(self.board.food)
            print(self.board.food)
            pygame.draw.rect(self.dis, green, [self.board.food[0] * self.blockSize, self.board.food[1] * self.blockSize, self.blockSize, self.blockSize])
            self.snake.render(self.dis, self.blockSize, (0,255,0), (50, 150, 50))
            # snake_Head = []
            # snake_Head.append(x1)
            # snake_Head.append(y1)
            # snake_list.append(snake_Head)
            #adds the snake head to the end of the list,

            # if len(snake_list) > snake_length:
                # del snake_list[0]

            # for x in snake_list[:-1]:
                # if x == snake_Head:
                    # print("collide")
                    # self.game_over= True  
            self.snake.move()
            if self.board.hitWall(self.snake.headPos) or self.snake.collision:
                self.game_over = True
            # if self.snake.headPos[0] >= self.num_cols or self.snake.headPos[0] < 0 \
                    # or self.snake.headPos[1] >= self.num_rows or self.snake.headPos[1] < 0:
                # self.game_over = True

#should i updatw after?
            pygame.display.update()
            if self.snake.headPos == self.board.food:
                self.board.genRandFood()
                print("Yummy!!")
            else:
                self.snake.removeTail()
            self.clock.tick(self.snakeSpeed)
#updates screen, only updates par that are passed, no par = entire screen
        pygame.quit()
        quit()
if __name__ == "__main__":
    g = snakeGame()
    g.gameLoop()
