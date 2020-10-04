#!/usr/bin/python3


class square():
    def __init__(self, size=0, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.size = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.size, self.size)

if __name__ == "__main__":

    s = square(size=10)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
