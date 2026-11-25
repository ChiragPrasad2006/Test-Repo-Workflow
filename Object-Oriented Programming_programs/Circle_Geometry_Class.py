import math
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    def get_area(self) -> float:
        return math.pi * self.radius * self.radius
    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius
