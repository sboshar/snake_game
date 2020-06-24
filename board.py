import random
import numpy as np
import pygame
from snake import Snake
#think about what defines a stat
#make this should be more like snakEnv rather than board
class Board:
    def __init__(self, r, c):
        #width and height refer to the number of squares
        #on the board, w * h = number of availPos
        self.num_rows = r
        self.num_cols = c
        self.food = self.genRandFood() 
        #self.board = 
        #self.board[self.food] = -1

    def shape(self):
        return (self.num_rows, self.num_cols)
    
    def genRandFood(self):
        self.food = (random.randint(0, self.num_rows), random.randint(0, self.num_cols))
        return self.food
        
    def reset(self):
        self.food = self.genRandFood()

    #not sure if needed in here
    def hitWall(self, pos):
        print(pos)
        return pos[0] < 0 or pos[0] >= self.num_cols or \
                pos[1] < 0 or pos[1] >= self.num_rows

    def printBoard(self, snake=None):
        b = []
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                s = (r,c)
                if snake and s in snake.segments:
                    b.append('s')
                elif s == self.food:
                    b.append('F')
                else:
                    b.append('☐')
        print(np.array(b).reshape(self.num_rows, self.num_cols))

    def render(self, win, block_size):
        pass
        
if __name__ == "__main__":
    board_rows = 20
    board_cols = 10
    #snake(colpos/x, rowpos/y)
    s = Snake((5,8))
    b = Board(board_rows, board_cols)
    b.food = (1, 8)
    b.printBoard(s)
