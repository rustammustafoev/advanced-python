## Supercharging Classes With Python super()
The `super()` keyword allows us to call parent class method from a child class
## Single Inheritance
```python
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getCircumference(self):
        return (self.height + self.width) * 2

    def getArea(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


class Cube(Square):
    def getSurfaceArea(self):
        face = super().getArea()
        return face * 6

    def getVolume(self):
        face = super().getArea()
        return face * self.height
```
