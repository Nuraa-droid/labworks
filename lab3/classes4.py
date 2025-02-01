import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, otherPoint):
        return math.sqrt((self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2)
    
p1 = Point(int(input()), int(input()))
p2 = Point(int(input()), int(input()))
p1.show()
p2.show()
print(p1.dist(p2))

