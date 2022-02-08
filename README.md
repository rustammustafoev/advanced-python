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
## C3 Linearization (Method Resolution Order)
```python
class D(object):
    pass

class F(object):
    pass

class C(object):
    pass

class B(D, F):
    pass

class A(B, C):
    pass
"""
    MRO logic under the hood
L[D(O)] = D + merge(L[O], O) = DO
L[F(O)] = FO
L[C(0)] = CO
L[B(D, F)] = B + merge(L[D], L[F], DF) = B + merge(DO, FO, DF) = B + D + merge(O, FO, F) + B + D + F + O = BDFO
L[A(B, C)] = A + merge(L[B], L[C], BC) = A + merge(BDFO, CO, BC) = A + B + merge(DFO, CO, C) = \
= A + B + D + merge(FO, CO, C) = A + B + D + F + merge(O, CO, C) + A + B + D + F + C + O = ABDFCO  # result
"""

print(A.__mro__)  # comparing our result with the built-in method
```
## Closures
```python
"""
Closure is an inner or nested function that carries information about its enclosing scope, even though this scope has completed its execution. We can reuse as much as we want because they don't forget their respective state information
"""

# Calculating the mean of some sample data
def mean():
    sample = []

    def _mean(number):
        sample.append(number)
        print(sample)
        return sum(sample) / len(sample)

    return _mean
current_mean = mean()
print(current_mean(10))
print(current_mean(15))
print(current_mean(12))
print(current_mean(11))
```
