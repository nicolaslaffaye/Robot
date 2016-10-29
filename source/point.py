"""
    ------------------------------------------
The class Point implements the object Point and its methods
A Point has two attributes:
    Args:
        x (int): position on X Axis.
        y (int): position on Y Axis.

    ------------------------------------------
"""

class Point(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	"""
	------------------------------------------
	_add_ redefine the normal addition in the point case
	
	Args:
		other (Point)

	Returns:
		the sum of the two points (the sum of each value on each Axis)
	------------------------------------------
	"""
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	"""
	------------------------------------------
	_ge_ redefine the normal greater or equal function for a Point
	
	Args:
		other (Point)

	Returns:
		True if both X Axis and Y Axis values of other are smaller than self
	------------------------------------------
	"""
	def __ge__(self, other):
		return self.x >= other.x and self.y >= other.y

	"""
	------------------------------------------
	_le_ redefine the normal lower or equal function for a Point
	
	Args:
		other (Point)

	Returns:
		True if both X Axis and Y Axis values of other are bigger than self
	------------------------------------------
	"""
	def __le__(self, other):
		return self.x <= other.x and self.y <= other.y

