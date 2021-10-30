from enum import Enum
import SnakeGame.Point as Point

class SnakeDirection(Enum):

    NORTH = Point(0,-1)
    EAST = Point(1,0)
    SOUTH = Point(0,1)
    WEST = Point(-1,1)

class Snake:

    def __init__(self,x:int,y:int):
        self.__head = Point(x,y)
        self.__tail = []
        self.__direction = SnakeDirection.NORTH

    def update(self,*,grow:bool=False):
        '''Update the snake.

        :param grow: If true, "grow" the snake by not popping it's tail.
        :type grow: bool
        '''
        self.__tail.append(self.__head.copy())
        self.__head += self.__direction
        if(not grow):
            self.__tail.pop()

    @property
    def head(self):
        return self.__head

    def overlaps(self,point:Point.Point) -> bool:
        '''Check if the Snake's tail or head overlaps a specific Point.

        :param point: Point to check.
        :type point: Point
        :returns: Whether or not the point is overlapped by the Snake's head or tail.
        :rtype: bool
        '''

        for segment in self.__tail:
            if point == segment:
                return True
        return point == self.__head

    def eating_self(self) -> bool:
        '''Check if the Snake's head is overlapping any of it's tail.

        :returns: Whether or not the head point overlaps any of the tail points.
        :rtype: bool
        '''

        for segment in self.__tail:
            if segment == self.__head:
                return True
        return False