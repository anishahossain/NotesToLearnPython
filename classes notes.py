class Point:  # class with block of specific functions
    # attribute are always defined using __init__ method not in class name

    origin = 0.0  # this is a class attribute

    def __init__(self, x, y):  # Initializes an object
        # so that we can pass parameters when creating object (its attributes)
        # self refers to current object (itself) and should be very first parameter of every method
        self.co_x = x  # argument x
        self.y = y  # argument y
        # a common practice is to name the attributes and parameters the same to about confusion

    def moving(self):  # function defined within class is an 'instance method'
        print('move')

    def drawing(self):
        print('draw')

# The term "hidden data members" typically refers to class attributes or variables
# that are not meant to be accessed directly from outside the class (using conventional dot notation).
# Instead, they are typically accessed and modified through class methods.

print(Point.origin)
# prints the class attribute

class Shape:
    default_color = 'red'

    def __init__(self):
        self.color = self.default_color

shape1 = Shape()
Shape.default_color = 'indigo'
# class attributes can be changed/updated
shape2 = Shape()

print(shape1.color)  # prints red as created before the class attribute was changed
print(Shape.default_color)  # prints indigo
print(shape2.color)  # prints indigo

point1 = Point(10, 20)  # defining an object which belongs to the 'Point' class
point1.moving()  # calling a function from our class using our object
point1.x = 10
point1.y = 20  # these are attributes we set for our specific object
print(point1.x)  # prints the attribute '10'

point2 = Point(10, 20)
print(point2.co_x)  # co_x attribute defined in constructor method
point2.co_x = 11  # attributes can be changed


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi! I am {self.name}')
        # allows us to use attribute made by using constructor method


anisha = Person('Anisha')  # attribute parameters initialized are passed like this
anisha.talk()


# Inheritance - is/a relationship 
class Mammal:  # this is the base class
    def __init__(self, color):
        # __init__() has no parameters except self, thus Mammal() creates an empty instance of Mammal.
        # no need to pass arguments when creating object
        self.color = color

    def noise(self, sound):
        print(sound)


    def walk(self):
        print('walk')




class Dog(Mammal):  # inherits methods from base class

    def __init__(self, size, color):
        super().__init__(color)
        # The super() function is used to give access to methods and properties of a parent or sibling class
        # however all parameters need to passed when defining the __init__() method
        self.size = size
    # When derived class defines a method having the same name as a method in the base class
    # Such a member function overrides the method of the base class.

    def noise(self, sound):
        Mammal.noise(self, sound)
        # when we want to call method from base class, format = BaseClass.method(self, parameters(if any))
        print('woof')
        # and also add any updates we want
dog = Mammal()
dog.noise('bark')  # argument can be passed here since the instance method contains a parameter


class Time:
    def __init__(self, hours, minutes):
        # Initializes a Time object with hours and minutes.
        self.hours = hours
        self.minutes = minutes

    def __str__(self):  # this is a special method that lets us customise the class (print customised messages)
        # Returns a string representation of the time in HH:MM format
        # __str__() method only takes self as an argument andno other
        return f'{self.hours}:{self.minutes}'

    def __lt__(self, other):  # this is a rich comparison method
        # Compares two Time objects to check if one time is earlier than the other
        # It checks if the hours of the current object (self.hours) are less than the hours of the other object
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            # If the hours are the same, it further compares the minutes
            if self.minutes < other.minutes:
                return True
        return False

num_times = 3
times = []

# Obtain times from user input
for i in range(num_times):
    user_input = input('Enter time (Hrs:Mins): ')
    tokens = user_input.split(':')  # splits hrs and mins into list items
    times.append(Time(int(tokens[0]), int(tokens[1]))) # appends them to times empty list

# The comparison of the time objects is performed without explicitly creating an object
# This is possible because the methods in the class are used within the context of the list operations and comparisons
min_time = times[0]
for t in times:
    if t < min_time:
        min_time = t

print(f'\nEarliest time is {min_time}')

# print(tuesday_time == workday) prints True/False (boolean value)

# other rich comparison methods
# __lt__(self, other)	less than (<)
# __le__(self, other)	less than or equal to (<=)
# __gt__(self, other)	greater than (>)
# __ge__(self, other)	greater than or equal to (>=)
# __eq__(self, other)	equal to (==)
# __ne__(self, other)	not equal to (!=)

#Example
class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def __lt__(self, other):
        if self.base < other.base:
            return True
        elif self.height < other.height:
            return True
        return False

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        # we refer back to the self.attributes initialized in classes
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    user_base1 = float(input())
    user_height1 = float(input())
    user_base2 = float(input())
    user_height2 = float(input())

    triangle1.set_base(user_base1)
    triangle1.set_height(user_height1)
    triangle2.set_base(user_base2)
    triangle2.set_height(user_height2)


    print('Triangle with smaller area:')
    ta1 = triangle1.get_area()
    ta2 = triangle2.get_area()
    # we have to include the if-else statement too even after using a rich comparison method
    if ta1 < ta2:
        triangle1.print_info()
    else:
        triangle2.print_info()




