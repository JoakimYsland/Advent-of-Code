
# 2D List
width, height = 10, 10
cave = [['.'] * width for i in range(height)]

# Basic 2D Vector Class
class Vec2:
	def __init__(self, x, y): 
		self.x = x
		self.y = y
	def __str__(self):
		s = "{0},{1}"
		return s.format(self.x, self.y)
	def __add__(self, v): 
		return Vec2(self.x + v.x, self.y + v.y)

# Basic 3D Vector Class
class Vec3:
	def __init__(self, x, y, z): 
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		s = "{0},{1},{2}"
		return s.format(self.x, self.y, self.z)
	def __add__(self, v): 
		return Vec2(self.x + v.x, self.y + v.y, self.z + v.z)

# Named Tuple
from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
new_student = Student('Bob', 19)