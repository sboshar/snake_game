import random
import pygame
from collections import deque
import numpy as np
import sys
#get the game working first, then implement it as 
#a oop so dont have to always render
class Snake:
    #init a snake in the middle, length three
    #moving downward
    def __init__(self, startPos):
        self.direction = (0, 1)
        self.alive = True
        self.headPos = startPos
        #just one segment long
        tail = self.getNextHead((0, -2))
        mid = self.getNextHead((0, -1))
        #head is at the end of the list
        self.segments = deque()
        self.segments.append(tail)
        self.segments.append(mid)
        self.segments.append(self.headPos)

    def __str__(self):
        return str(self.segments)

    def __len__(self):
        return len(self.segments)
    
    def setDirection(self, d):
        self.direction = d 

    def getDirection(self):
        return self.direction

    #maybe this should jsut return pos of first element
    def getHeadPos(self):
        return (self.headRow, self.headCol)

    def getSegments(self):
        return self.segments

    def setHeadPos(self, v):
        self.headPos = v 

    def removeTail(self):
        self.segments.popleft()
    
    def getNextHead(self, d):
        return (self.headPos[0] + d[0], self.headPos[1] + d[1])
    #adds direction to
    #should the check for food be in the main class,
    # seems a little weird we pass food into snake move
    def move(self, food):
        #set the next head pos
        self.setHeadPos(self.getNextHead(self.direction))
        #add the head to the front of the queue
        self.segments.append(self.headPos)
        if self.headPos != food:
            _ = self.removeTail()
    
    def render(self, win, block_size, color):
        for seg in self.segments:
            #draw the snake
            pygame.draw.rect(win, color, (seg[0] * block_size, seg[1] * block_size,
                block_size, block_size)) 
        
if __name__ == "__main__":
    pygame.init()
    WIDTH = 500
    HEIGHT = 500
    VELOCITY = 5
    block_size = 10
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    s = Snake((10, 10))
    g = False
    while not g:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g = True
            if event.type == pygame.KEYDOWN:
                print(s)
                s.move((0,0))
            win.fill((0,0,0))
            s.render(win, 10, (0, 255, 0))
            pygame.display.update()
    #pygame.init()
    #window = pygame.display.set_mode((400,400))
    #pygame.display.set_caption("Snake")
