class Rectangle:
    # When a Rectangle object is created, it should be initialized with width and height attributes.
    def __init__(self, width, height):
        self.height = height
        self.width = width

    # a string, it should look like: Rectangle(width=5, height=10)
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + "," + " height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width
        pass

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        result = ""
        if self.height >=50:
            return "Too big for picture."
        if self.width >=50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                result += "*"
            result += "\n"
        print(result)
        return result

    #Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape
    # could fit inside the shape (with no rotations).
    # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    def get_amount_inside(self, rectangle):
        take_height = rectangle.height
        take_width = rectangle.width
        if take_height <= self.height:
            if take_width <= self.width:
                #will not work properly in some cases
                return self.get_area() // rectangle.get_area()
            else:
                return 0
        return 0


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    # a string, it should look like: Rectangle(width=5, height=10)
    def __str__(self):
        return "Square(side=" + str(self.height) + ")"

    def set_side(self, side_length):
        self.height = side_length
        self.width = side_length

    def set_width(self, side_length):
        self.height = side_length
        self.width = side_length

    def set_height(self, side_length):
        self.height = side_length
        self.width = side_length