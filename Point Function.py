class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"(x = {self.x}, y = {self.y})"
    
p1 = Point(2, 3)
p2 = Point(25, 36)

print(p1)
print(p2)
    