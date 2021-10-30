from dataclasses import dataclass

@dataclass(eq=True,order=False)
class Point:
    """
    Represents a point in 2D space.

    :field x: The x coordinate of the point.
    :type x: int
    :field y: The y coordinate of the point.
    :type y: int
    """

    x: int
    y: int

    def copy(self):
        '''Returns a copy of the point object.
        
        :returns copy: Copy of the point.
        :rtype: Point'''
        return Point(self.x,self.y)

    def __add__(self,other):
        if isinstance(other,Point):
            self.x += other.x
            self.y += other.y
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Point' and '{other.__class__.__name__}'")
    
    def __sub__(self,other):
        if isinstance(other,Point):
            self.x -= other.x
            self.y -= other.y
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Point' and '{other.__class__.__name__}'")
    