class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(f'Figura o środku w ({self.x}, {self.y}) koloru {self.color}')

    def distance(self, other): #other nazywamy sobie zmienna która będzie liprzymować wartość zadaną
        a = self.x - other.x
        b = self.y - other.y
        return (a**2 + b**2)**1/2 #pitagoras a2 + b2 = c2 albo math.sqrt((a**2 + b**2))

    def __str__(self):
        return f'Figura o środku w ({self.x}, {self.y}) koloru {self.color}'


triangle = Shape(3, 3, 'green')
square = Shape(5, 7, 'red')
circle = Shape(12, 3, 'green')
hexagon = Shape(11, 6, 'blue')

hexagon.describe()
#triangle.describe()
#circle.describe()
#hexagon.describe()

print(hexagon.distance(circle))
print(circle.distance(triangle))
print(circle.distance(square))

print(hexagon)

