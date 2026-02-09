Q6.Use abc module to create abstract class Shape with method area().
Ans:-
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        passclass Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())   # 78.5
