import SnakeGame.Snake as Snake
import SnakeGame.Point as Point
from random import randint, seed
from os import time
from enum import Enum

class TileType(Enum):

    EMPTY = 0
    HEAD = 1
    TAIL = 2
    APPLE = 3

class GameOver:
    '''GameOver class. Empty, but used to check if the Snake Game is over.'''
    pass

class SnakeGame:

    def __init__(self,board_size:int):
        seed(time())
        self.size = board_size
        self.apple = None
        self.snake = Snake(size//2,size//2)

    def spawn_apple(self):
        '''Spawns an apple on the board.'''

        while True:
            self.apple = Point.Random(0,self.size,0,self.size)

            if(not self.snake.overlaps(self.apple)):
                break
        
    def update(self):
        '''Updates the game. If there is no apple, spawn an apple. Update the snake. If the snake is overlapping itself, call SnakeGame.game_over()'''

        if self.apple == None:
            self.spawn_apple()
        self.snake.update(grow=self.snake.overlaps(self.apple))

        if(self.snake.eating_self):
            self.game_over()

    def game_over(self):
        '''Ends the game.

        :raises GameOver: Raises a GameOver class to be caught and handled by the Game driver.
        '''

        raise GameOver()

    def tile_type(self,point:Point.Point) -> TileType:
        '''Checks if a point is on the game board.

        :param point: Point to check
        :type point: Point
        :returns: What kind of tile the specific point is.
        :rtype: TileType
        '''

        if(point == self.apple):
            return TileType.APPLE
        elif(self.snake.overlaps(point)):
            if point == self.snake.head:
                return TileType.HEAD
            else:
                return TileType.TAIL
        else:
            return TileType.EMPTY
        