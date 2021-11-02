from enum import Enum
import SnakeGame.Point as Point
class SnakeDirection(Enum):
    '''Directions a Snake's head can face.

    Includes NORTH, EAST, SOUTH, WEST'''

    NORTH = Point.Point(0,-1)
    EAST = Point.Point(1,0)
    SOUTH = Point.Point(0,1)
    WEST = Point.Point(-1,1)

class Snake:
    '''SnakeGame Snake object.
    
    :ivar head: The head of the Snake.
    :vartype head: Point
    :ivar length: Length of the Snake.
    :vartype length: int'''

    def __init__(self,x:int,y:int):
        self.__head = Point.Point(x,y)
        self.__tail = []
        self.__direction = SnakeDirection.NORTH

    def update(self,*,grow:bool=False):
        '''Update the snake.

        :param grow: If true, "grow" the snake by not popping it's tail.
        :type grow: bool
        '''
        self.__tail.append(self.__head.copy())
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