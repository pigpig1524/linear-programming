from point import Point

class Function:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, point: Point):
        return self.a * point.x + self.b * point.y

class Equation:
    """
    The equation's form is ax + by = c
    """
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b
        self.c = c

    def solve(self, other: "Equation"):
        if not other:
            print("Don phuong trinh")
        else:
            print("he phuong trinh")

# class Line:
#     def __init__(self, a, b, c):
#         """
#         Function's form: ax + by = c
#         """
#         self.a = a
#         self.b = b
#         self.c = c

#     def intersect(self, other: "Line"):        
#         pass

class Line(Equation):
    def __init__(self, p1: Point, p2: Point):
        # super().__init__(a, b, c)
        pass

    def intersect(self, other: "Line"):
        return self.solve(other)
    
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    line = Line()
