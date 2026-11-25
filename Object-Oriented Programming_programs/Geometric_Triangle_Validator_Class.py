class Triangle:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    def classify(self) -> str:
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            return "Invalid"
        if self.x + self.y <= self.z:
            return "Invalid"
        if self.x + self.z <= self.y:
            return "Invalid"
        if self.y + self.z <= self.x:
            return "Invalid"
        if self.x == self.y == self.z:
            return "Equilateral"
        if self.x == self.y or self.x == self.z or self.y == self.z:
            return "Isosceles"
        return "Scalene"
