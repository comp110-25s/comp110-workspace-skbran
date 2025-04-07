# Magic Methods

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # specify what we want to be printed when we call this class
    def __str__(self) -> str:  # dev a method that doesn't explicitly have to be called
        """Magic method that will print str representation of a Point object"""
        return f"({self.x}, {self.y})"

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5
    
    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy

pt: Point = Point(2.0, 1.0)

print(Point)
