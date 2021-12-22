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
## Multiple Inheritance
To inspect what will be called first when ``super()`` used we use ``className.__mro__``
```python
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
        
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
```
