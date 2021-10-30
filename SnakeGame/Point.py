from dataclasses import dataclass

class Point:

    x: int
    y: int

    def copy(self):
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
    