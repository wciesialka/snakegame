from enum import Enum
import SnakeGame.Point as Point
from typing import List
class SnakeDirection(Enum):
    '''Directions a Snake's head can face.

    Includes NORTH, EAST, SOUTH, WEST'''

    NORTH = Point.Point(0,-1)
    EAST = Point.Point(1,0)
    SOUTH = Point.Point(0,1)
    WEST = Point.Point(-1,0)

class Snake:
    '''SnakeGame Snake object.
    
    :ivar head: The head of the Snake.
    :vartype head: Point
    :ivar length: Length of the Snake.
    :vartype length: int'''

    def __init__(self,x:int,y:int):
        self.__head:Point.Point = Point.Point(x,y)
        self.__tail:List[Point.Point] = []
        self.__direction:SnakeDirection = SnakeDirection.NORTH

    def update(self,*,grow:bool=False):
        '''Update the snake.

        :param grow: If true, "grow" the snake by not popping it's tail.
        :type grow: bool
        '''
        self.__tail.insert(0,self.__head.copy())
        self.__head += self.__direction.value
        if(not grow):
            self.__tail.pop()

    @property
    def head(self) -> Point.Point:
        '''Head of the Snake.'''
        return self.__head

    @property
    def length(self) -> int:
        '''Length of the Snake.'''
        return 1 + len(self.__tail)

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

    def is_eating_self(self) -> bool:
        '''Check if the Snake's head is overlapping any of it's tail.

        :returns: Whether or not the head point overlaps any of the tail points.
        :rtype: bool
        '''

        for segment in self.__tail:
            if segment == self.__head:
                return True
        return False

    def is_facing(self,direction:SnakeDirection) -> bool:
        '''Check if Snake is facing a direction.

        :param direction: Direction to check.
        :type direction: SnakeDirection
        :returns: True if Snake is facing that direction, False otherwise.
        :rtype: bool
        '''

        return self.__direction == direction

    def is_facing_north(self) -> bool:
        '''Check if Snake is facing North.

        :returns: True if Snake is facing North, False otherwise.
        :rtype: bool
        '''

        return self.is_facing(SnakeDirection.NORTH)

    def is_facing_east(self) -> bool:
        '''Check if Snake is facing East.

        :returns: True if Snake is facing East, False otherwise.
        :rtype: bool
        '''

        return self.is_facing(SnakeDirection.EAST)

    def is_facing_west(self) -> bool:
        '''Check if Snake is facing West.

        :returns: True if Snake is facing West, False otherwise.
        :rtype: bool
        '''

        return self.is_facing(SnakeDirection.WEST)

    def is_facing_south(self) -> bool:
        '''Check if Snake is facing South.

        :returns: True if Snake is facing South, False otherwise.
        :rtype: bool
        '''

        return self.is_facing(SnakeDirection.SOUTH)

    def face_direction(self,direction:SnakeDirection):
        '''Make the head of the snake face a certain direction.

        :param direction: Direction to face
        :type direction: SnakeDirection'''
        if isinstance(direction,SnakeDirection):
            self.__direction = direction
        else:
            raise TypeError(f'Expected enum SnakeDirection, not type {direction.__class__.__name__}')

    def face_north(self):
        '''Make the head of the snake face north.'''
        self.face_direction(SnakeDirection.NORTH)

    def face_east(self):
        '''Make the head of the snake face east.'''
        self.face_direction(SnakeDirection.EAST)

    def face_south(self):
        '''Make the head of the snake face south.'''
        self.face_direction(SnakeDirection.SOUTH)

    def face_west(self):
        '''Make the head of the snake face west.'''
        self.face_direction(SnakeDirection.WEST)