class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        else:
            pic = ''
            for i in range(self.height):
                pic += self.width*'*'
                pic += '\n'
            return pic

    def get_amount_inside(self, other):
        amount = (self.get_area()) / (other.get_area())
        width_times = self.width // other.width
        height_times = self.height // other.height
        if amount.is_integer():
            return amount
        else:
            if width_times < height_times:
                return width_times
            else:
                return height_times

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})' 
    
class Square(Rectangle):    
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_side):
        self.side = new_side
        super().set_width(new_side)
        super().set_height(new_side)

    def set_width(self, new_width):
        self.side = new_width
        super().set_width(new_width)
        super().set_height(new_width)

    def set_height(self, new_height):
        self.side = new_height
        super().set_width(new_height)
        super().set_height(new_height)

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.side})"

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.side})"