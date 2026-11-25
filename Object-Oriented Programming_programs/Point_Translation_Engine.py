class CoordinateNormalizer:
    def __init__(self, coordinates: list[tuple[int, int]]):
        self.coordinates = coordinates
    def normalize(self) -> list[tuple[int, int]]:
        smallest_x = min(point[0] for point in self.coordinates)
        smallest_y = min(point[1] for point in self.coordinates)
        return [
            (x - smallest_x, y - smallest_y)
            for x, y in self.coordinates
        ]
