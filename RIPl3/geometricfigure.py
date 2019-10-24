from abc import *
import math
import random


class Geometric_figure(ABC):
    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def area(self):
        pass
    pass

class ColorFigure:
	def __init__(self):
		self.color = None
		pass

	@property
	def colorproperty(self):
		return self.color
		pass

	@colorproperty.setter
	def colorproperty(self, color):
		self.color = color
		pass
	pass

class Rectangle(Geometric_figure):
	def __init__(self, width, high, color):
		super().__init__("прямоугольник")
		self.width = width
		self.high = high
		self.col = ColorFigure()
		self.col.colorproperty = color
		pass

	def area(self):
		return self.width * self.high
		pass

	def __repr__(self):
		return "Площадь {} {}а высотой {} и шириной {} равна {}"\
			.format(  self.col.colorproperty, self.name,self.high, self.width, self.area())
		pass

	pass

class Square(Rectangle):
	FIGURE = "квадрат"

	@classmethod
	def get_figure_type(cls):
		return cls.FIGURE

	def __init__(self, x, color):
		self.x = x
		self.col = ColorFigure()
		self.col.colorproperty = color
		pass

	def area(self):
		return self.x * self.x
		pass

	def __repr__(self):
		return "Площадь {} {}а длиной {} равна {}"\
			.format( self.col.colorproperty, self.get_figure_type(), self.x , self.area())
		pass

	pass


class Circle(Geometric_figure):
	def __init__(self, radius, color):
		super().__init__("круг")
		self.radius = radius
		self.fc = ColorFigure()
		self.fc.colorproperty = color
		pass

	def area(self):
		return math.pi * (self.radius ** 2)
		pass

	def __repr__(self):
		return "Площадь {} {}а радиуса {} равна {}"\
			.format( self.fc.colorproperty, self.name, self.radius, self.area())
		pass

	pass

figurecolors = ("красного", "оранжевого", "желтого", "зеленого",  "голубого", "синего", "фиолетового" )
rc=random.choice(figurecolors)
cc=random.choice(figurecolors)
sc=random.choice(figurecolors)
def main():

	rect = Rectangle( random.randint(1,9),  random.randint(1,9), rc)
	print(rect)
	circle = Circle( random.randint(1,9), cc)
	print(circle)
	square = Square( random.randint(1,9), sc)
	print(square)

if __name__ == "__main__":
	main()
