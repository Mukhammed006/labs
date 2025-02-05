#1
class Person:
    def __init__(self, n):
        self.name = n

    def inp(self):
        self.n = input()

    def __str__(self):
        print(self.n.upper())
noname = Person("Me")
noname.inp()
noname.__str__()
# #2
# class Shape:
#     def area(self, a=0):
#         print(a)

# class Square(Shape):
#     def __init__(self, length):
#         self.l=length
# s = Square(5465)
# s.area()

# #3
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.l=length
#         self.w=width
#     def area(self):
#         return self.l*self.w
    
# r=Rectangle(12 ,5)
# print(r.area())