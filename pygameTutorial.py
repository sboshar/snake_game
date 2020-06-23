import pygame
import random
from snake import Snake
pygame.init()
WIDTH = 500
HEIGHT = 500
VELOCITY = 5
block_size = 10
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("first game")


def gameLoop():
    game_over = False
    #snake = Snake((WIDTH//2, HEIGHT//2))
    
    snake  = Snake((10, 10))
    #location on the grid not actually in space
    food = (10, 10)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.getDirection() != (0, 1):
                    snake.setDirection((0,-1))
                    snake.move(food)
                elif event.key == pygame.K_DOWN and snake.getDirection() != (0, -1):
                    snake.setDirection((0,1))
                    snake.move(food)
                elif event.key == pygame.K_LEFT and snake.getDirection() != (1,0):
                    snake.setDirection((-1,0))
                    snake.move(food)
                elif event.key == pygame.K_RIGHT and snake.getDirection() != (-1, 0):
                    snake.setDirection((1,0))
                    snake.move(food)
            win.fill((0,0,0))
            pygame.draw.rect(win, (255, 0, 0), [block_size * food[0], 
                block_size * food[1], block_size, block_size])
            snake.render(win, block_size, (0, 255, 0))
            pygame.display.update()
            
                    
if __name__ == "__main__":
    gameLoop()
