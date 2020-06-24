import pygame
import random
from snake import Snake

##really slow right now, wonder if it has to do with update,
# need to check against other program

class snakeGame(object):

    def __init__(self):
        pygame.init()
        #pixel width and height
        self.PIXELWIDTH = 500
        self.PIXELHEIGHT = 500

        #dim of the board
        self.xdim = 20
        self.ydim = 20
        self.VELOCITY = 5
        self.block_size = self.PIXELWIDTH // self.xdim  
        #snake takes the coordniate pos not the pixel ones
        self.snake = Snake((self.xdim//2, self.ydim//2))
        self.snakeSpeed = 5
        #location on the board not in pixels
        #right now this doesnt take into account the 
        #location of the snake
        self.randFood()
        self.game_over = False
        self.win = pygame.display.set_mode((self.PIXELWIDTH, self.PIXELHEIGHT))
        #not sure if I want thid
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("snake game")

    def randFood(self):
        loc = (random.randrange(0, 10), random.randrange(0,10)) 
        while loc in self.snake.segments:
            loc = (random.randrange(0, 10), random.randrange(0,10)) 
        self.food = loc
         
    def run(self): 
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.getDirection() != (0, 1):
                        self.snake.setDirection((0,-1))
                    elif event.key == pygame.K_DOWN and self.snake.getDirection() != (0, -1):
                        self.snake.setDirection((0,1))
                    elif event.key == pygame.K_LEFT and self.snake.getDirection() != (1,0):
                        self.snake.setDirection((-1,0))
                    elif event.key == pygame.K_RIGHT and self.snake.getDirection() != (-1, 0):
                        self.snake.setDirection((1,0))
            self.snake.move(self.food)
            #maybe the key is to handle the remove tail
            #function down here so dont have to pass in food
            if self.snake.getHeadPos() == self.food:
                self.randFood()

            self.win.fill((0,0,0))
            pygame.draw.rect(self.win, (255, 0, 0), [self.block_size * self.food[0], 
                self.block_size * self.food[1], self.block_size, self.block_size])
            self.snake.render(self.win, self.block_size, (0, 255, 0),(34,139,34))
            pygame.display.update()

            self.clock.tick(self.snakeSpeed)
            
                    
if __name__ == "__main__":
    game = snakeGame()
    game.run()
