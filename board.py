import random
import pygame
from snake import Snake
#think about what defines a stat
#make this should be more like snakEnv rather than board
class Board:
    def __init__(self, width, height, snake):
        #width and height refer to the number of squares
        #on the board, w * h = number of availPos
        self.width = width
        self.height = height
        self.snake = snake
        self.food = (random.randint(0, width - 1), random.randint(0, height - 1))
        #self.board = np.zeros((self.width, self.height)) 
        #self.board[self.food] = -1

    def reset(self):
        self.snake = Snake((self.width//2, self.height//2))
        return self.snake

    def isTerminal(self, pos):
        return pos[0] < 0 or pos[0] > self.width or \
                pos[1] < 0 or pos[1] > self.height

    #returns next state, reward, done
    def step(self, direction):
        pass

    #def printBoard(self, isFull=False):
    #    if isFull:
    #        np.set_printoptions(threshold=sys.maxsize)
        #print(self.board)

    #def drawSnake(self):
    #    for i in self.snake.getSegments():
    #        self.board[i] = 1


if __name__ == "__main__":
    boardX = 10
    boardY = 10
    snake = Snake((5,5))
    b = Board(boardX, boardY, snake)

