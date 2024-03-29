import SnakeGame.Snake as Snake
import SnakeGame.Point as Point
from random import randint, seed
from time import time_ns
from enum import Enum
from typing import Tuple

class TileType(Enum):
    '''Types of Tiles that a SnakeGame can have on it's board.
    
    Includes EMPTY, HEAD, TAIL, APPLE'''

    EMPTY = 0
    HEAD = 1
    TAIL = 2
    APPLE = 3

class GameOver(BaseException):
    '''GameOver class. Empty, but used to check if the Snake Game is over.'''
    pass

class SnakeGame:
    '''SnakeGame controller.'''

    def __init__(self,board_size:Tuple[int,int],initial_snake_size:int = 1,game_seed:int = time_ns()):
        seed(game_seed)
        self.__size:Tuple[int,int] = board_size
        self.__apple:Point.Point = None
        self.__snake:Snake.Snake = Snake.Snake(self.__size[0]//2,self.__size[1]//2)
        self.__initial_size:int = initial_snake_size
        self.__growths:int = initial_snake_size-1 # -1 because we want the tail size

        self.__spawn_apple()

    @property
    def score(self) -> int:
        '''The score of the game.'''
        return self.__snake.length - self.__initial_size

    @property
    def size(self) -> int:
        '''The size of the board.'''
        return self.__size

    def __spawn_apple(self):
        '''Spawns an apple on the board.'''

        while True:
            self.__apple = Point.Point.Random(0,0,self.__size[0],self.__size[1])

            if(not self.__snake.overlaps(self.__apple)):
                break
        
    def update(self):
        '''Updates the game. If there is no apple, spawn an apple. Update the snake. If the snake is overlapping itself, call SnakeGame.game_over()'''

        if self.__apple == None: # handle if there is no apple
            self.__spawn_apple()


        if(self.__snake.head.x < 0 or self.__snake.head.x > self.size[0]
        or self.__snake.head.y < 0 or self.__snake.head.y > self.size[1]
        or self.__snake.is_eating_self()): # handle oob and eating self
            self.game_over()

        if self.__growths > 0: # handle if snake does not eat apple
            self.__snake.update(grow=True)
            self.__growths -= 1
        else:
            self.__snake.update(grow=False)

        if self.__snake.overlaps(self.__apple): # handle if snake eats apple
            self.__growths += 1
            self.__spawn_apple()

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
        
    def face_north(self):
        '''Make the Snake face North. Cannot face North if currently facing South.'''
        if not self.__snake.is_facing_south():
            self.__snake.face_north()

    def face_east(self):
        '''Make the Snake face East. Cannot face East if currently facing West.'''
        if not self.__snake.is_facing_west():
            self.__snake.face_east()

    def face_south(self):
        '''Make the Snake face South. Cannot face South if currently facing North.'''
        if not self.__snake.is_facing_north():
            self.__snake.face_south()

    def face_west(self):
        '''Make the Snake face West. Cannot face West if currently facing East.'''
        if not self.__snake.is_facing_east():
            self.__snake.face_west()