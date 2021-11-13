# import math
# class House:
#     windows_count: int
#     area: float
#
#     def __init__(self, windows_count: int, area: float):
#         self.windows_count = windows_count
#         self.area = area
#
#     def change_area(self, area_to_add: float) -> None:
#         self.area += area_to_add
#
#     def __str__(self) -> str:
#         return f'liczba okien: {self.windows_count}, powierzchnia: {self.area}'
#
# #
# # h1 = House(15, 120.5)
# # print(h1.windows_count)
# #
# # h1.change_area(10.5)
# # print(h1.area)
# #
# # print(h1)
#
# class Square:
#     side: float
#
#     def __init__(self, side: float):
#         self.side = side
#
#     def area(self):
#         return self.side*self.side
#
#     def perimeter(self):
#         return self.side*4
#
#
# kwadrat = Square(4)
# print(kwadrat.perimeter())
#
#
# class Triangle:
#     side: float
#     height: float
#
#     def __init__(self, side, height):
#         self.side = side
#         self.height = height
#
#     def area(self):
#         return self.side*self.height/2
#
#     def perimeter(self):
#         return 2 * self.side + 5
#
#
# bill = Triangle(5,7)
# print(bill.height)
#
#
#
# kwadraty = []
# for i in range(11,20):
#     x = Square(i)
#     kwadraty.append(x)
#
#

class Tree:
    name: str
    height: float
    leafs: int

    def __init__(self, name: str, height: float, leafs: int):
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, growth: float) ->None:
        self.height += growth

    def grow_wide(self, new_leafs: int) ->None:
        self.leafs += new_leafs

    def show(self):
        print(f'nazwa = {self.name}, wysokość = {self.height}, liczba liści = {self.leafs}')


t1 = Tree('wiąz', 43.1, 2100)
t1.grow_up(0.4)
t1.grow_wide(37)
t1.show()


las = []
for i in range(5):
    x = Tree('drzewo'+str(i+1), 45-i, 1300+400*i)
    las.append(x)
    x.show()

print("\n")

for i in range(len(las)):
    las[i].grow_wide(123-i)
    las[i].show()
