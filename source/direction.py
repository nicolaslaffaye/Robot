"""
    ------------------------------------------
The class Direction implements the object Direction and all the compass methods
A Direction has one attribute:
    Args:
        cardinalDirection (String): ["EAST","NORTH","WEST","SOUTH"]

    ------------------------------------------
"""



from .point import Point
from math import pi,sin,cos

class Direction(object):
	
	
	def __init__(self, cardinalDirection):
		self.cardinalDirection = cardinalDirection
		self.dirs = ["EAST","NORTH","WEST","SOUTH"]
		
		
	"""
	------------------------------------------
	validateOrientation test if the parameter is valid
	
	Args:
		None

	Returns:
		True if the parameter is valid, False otherwise
	------------------------------------------
	"""
	def validateOrientation(self):
		return self.cardinalDirection in self.dirs

	"""
	------------------------------------------
	__getAngleFromOrientation__ is an internal function calculating an angle in degres from the cardinal direction
	
	Args:
		None

	Returns:
		The angle in between the X axis and the direction the robot faces
	------------------------------------------
	"""		
	def __getAngleFromOrientation__(self):
		return int(self.dirs.index(self.cardinalDirection)*90)

	"""
	------------------------------------------
	__getOrientationFromAngle__is an internal function calculating the cardinal direction from an angle
	
	Args:
		angle (int): Angle in between the X Axis and the direction the robot faces

	Returns:
		The cardinal direction (String)
	------------------------------------------
	"""			
	def __getOrientationFromAngle__(self,angle):
		return self.dirs[int(angle/90)]
		
		
	"""
	------------------------------------------
	rotateLeft is a function rotating clockwise our robot by 90 degres
	
	Args:
		None

	Returns:
		The new Direction (Direction)
	------------------------------------------
	"""	
	def rotateLeft(self):
		return Direction(self.__getOrientationFromAngle__(int((self.__getAngleFromOrientation__() + 90)%360)))


	"""
	------------------------------------------
	rotateRight is a function rotating counterclockwise our robot by 90 degres
	
	Args:
		None

	Returns:
		The new Direction (Direction)
	------------------------------------------
	"""			
	def rotateRight(self):
		return Direction(self.__getOrientationFromAngle__(int((self.__getAngleFromOrientation__() - 90)%360)))

		
	"""
	------------------------------------------
	getNextMove is a function calculating the next trajectory depending on the Direction
	
	Args:
		None

	Returns:
		a vector (Point) of what would be the next move
	------------------------------------------
	"""		
	def getNextMove(self):
		return Point(int(cos(pi/2*self.__getAngleFromOrientation__()/90)), int(sin(pi/2*self.__getAngleFromOrientation__()/90)))
