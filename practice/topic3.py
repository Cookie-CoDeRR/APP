from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class square(Shape):
    def __init__(self, side):
        self.side = side
        
    # FIX: Renamed from square_area to calculate_area
    def calculate_area(self): 
        return self.side * self.side

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # FIX: Renamed from circle_area to calculate_area
    def calculate_area(self): 
        return (self.radius * self.radius) * 3.14

my_square = square(4)
# Now this works perfectly!
print(my_square.calculate_area())