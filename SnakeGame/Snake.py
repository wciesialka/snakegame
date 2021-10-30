from enum import Enum
import SnakeGame.Point as Point

class SnakeDirection(Enum):

    NORTH = Point(0,-1)
    EAST = Point(1,0)
    SOUTH = Point(0,1)
    WEST = Point(-1,1)

class Snake:

    def __init__(self,x,y):
        self.__head = Point(x,y)
        self.__tail = []
        self.__direction = SnakeDirection.NORTH

    def update(self,*,grow=False):
        if(grow):
            self.__tail.append(self.__head.copy())
        else:
            self.__tail.append(self.__head.copy())
            self.__head += self.__direction
            self.__tail.pop()
