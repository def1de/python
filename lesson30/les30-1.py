class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def space(self):
        space = self.width*self.height
        print ('Space >>>', space)

width = int(input('Enter width >>> '))
height = int(input('Enter height >>> '))

rect = Rectangle(width, height)
rect.space()