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
        self.__size = board_size
        self.__apple = None
        self.__snake = Snake(self.__size//2,self.__size//2)
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @property
    def size(self):
        return self.__size

    def __spawn_apple(self):
        '''Spawns an apple on the board.'''

        while True:
            self.__apple = Point.Random(0,self.__size,0,self.__size)

            if(not self.__snake.overlaps(self.__apple)):
                break
        
    def update(self):
        '''Updates the game. If there is no apple, spawn an apple. Update the snake. If the snake is overlapping itself, call SnakeGame.game_over()'''

        if self.__apple == None: # handle if there is no apple
            self.__spawn_apple()

        if self.__snake.overlaps(self.__apple): # handle if snake eats apple
            self.__snake.update(grow=True)
            self.__score += 1
        else: # handle if snake does not eat apple
            self.__snake.update(grow=False)

        if(self.__snake.is_eating_self()): # handle if snake is overlapping itself
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


        if(self.__snake.overlaps(point)):
            if point == self.__snake.head:
                return TileType.HEAD
            else:
                return TileType.TAIL
        elif(point == self.__apple):
            return TileType.APPLE
        else:
            return TileType.EMPTY
        