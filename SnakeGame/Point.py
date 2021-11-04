from __future__ import annotations
from dataclasses import dataclass, fields
from random import randint

@dataclass(eq=True,order=False)
class Point:
    """
    Represents a point in 2D space.

    :ivar x: The x coordinate of the point.
    :vartype x: int
    :ivar y: The y coordinate of the point.
    :vartype y: int
    """

    x: int
    y: int
  
    @classmethod
    def Random(cls,x:int,y:int,dx:int,dy:int) -> Point:
        '''Returns a Point object with random x and y coordinates.

        :param x: Lower bound of x
        :type x: int
        :param dx: Possible range of change of x
        :type dx: int
        :param y: Lower bound of y
        :type y: int
        :param dy: Possible range of change of y
        :type dy: int

        :returns: A Point with random coordinates.
        :rtype: Point
        '''
        nx = randint(x,x+dx)
        ny = randint(y,y+dy)
        return cls(nx,ny)


    def copy(self) -> Point:
        '''Returns a copy of the point object.
        
        :returns copy: Copy of the point.
        :rtype: Point'''
        return Point(self.x,self.y)

    def __add__(self,other):
        if isinstance(other,Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x,y)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Point' and '{other.__class__.__name__}'")
    
    def __sub__(self,other):
        if isinstance(other,Point):
            x = self.x - other.x
            y = self.y - other.y
            return Point(x,y)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Point' and '{other.__class__.__name__}'")