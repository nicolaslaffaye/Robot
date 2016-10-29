from .point import Point

"""
    ------------------------------------------
The class robot implements the object robot and its command
A robot responds to the following commands:
PLACE, MOVE, LEFT, RIGHT and REPORT
    ------------------------------------------
"""

class robot(object):

    
	def __init__(self, support, position = Point(0,0), orientation = None):
		self.position = position                                                #Point object representing the robot position                                                           #Integer representing the robot position on the Y axis. Robot initially at origin (0,0)
		self.orientation = orientation                                          #Direction object representing the robot orientation WEST, EAST, NORTH or SOUTH
		self.support = support                                                  #MyPlatform object representing the platform the robot has been placed on


	"""
	------------------------------------------
	PLACE is the function placing the robot on the platform
	Args:
        support (MyPlatform): The platform object MyPlatform.
        position (Point): The position.
        orientation (Direction): The orientation object Direction.

	Returns:
        the robot placed
	------------------------------------------
	"""
	def PLACE(self, support, position, orientation):
		if support.testIfWithinBoundaries(position) and orientation is not None and orientation.validateOrientation():
			return robot(support, position, orientation)
		else:	
			return self



	"""
	------------------------------------------
	MOVE is the function moving the robot on the platform
	It increases the X or Y axis position by 1 depending on the orientation
	
	Args:
		NONE

	Returns:
		The robot with the new position if it can be placed
	------------------------------------------
	"""
	def MOVE(self):
		if self.orientation is not None and self.orientation.validateOrientation():
			return self.PLACE(self.support,self.position + self.orientation.getNextMove(), self.orientation)
		else:
			return self


	"""
	------------------------------------------
	LEFT is the function rotating the robot 90 degrees on the left
    
	Args:
		NONE

	Returns:
		the robot with the new orientation if valid
	------------------------------------------
	"""
	def LEFT(self):
		if self.orientation is not None and self.orientation.validateOrientation():
			return self.PLACE(self.support, self.position, self.orientation.rotateLeft())
		else:
			return self


	"""
	------------------------------------------
	RIGHT is the function rotating the robot 90 degrees on the right
    
	Args:
		NONE

	Returns:
		the robot with the new orientation if valid
	------------------------------------------
	"""
	def RIGHT(self):
		if self.orientation is not None and self.orientation.validateOrientation():
			return self.PLACE(self.support, self.position, self.orientation.rotateRight())
		else:
			return self


	"""
	------------------------------------------
	REPORT is the function outputing the robot current position and orientation
    
	Args:
		NONE

	Returns:
		the robot
	------------------------------------------
	"""
	def REPORT(self):
		if self.orientation is not None:
			print(self.position.x,self.position.y,self.orientation.cardinalDirection)
		return self

