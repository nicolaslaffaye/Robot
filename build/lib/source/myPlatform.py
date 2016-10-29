"""
    ------------------------------------------
The class myPlatform implements the object platform and its command
A platform has four attributes:
    Args:
        origin (Point): The origin for the platform.
        mrightUpperCorner (Point): The right extrem uper corner.

    ------------------------------------------
"""
class myPlatform:

	def __init__(self, origin, rightUpperCorner):
		self.origin = origin                                      
		self.rightUpperCorner = rightUpperCorner                                     


	"""
	------------------------------------------
	testIfWithinBoundaries is the function checking if a position in on the platform
	Args:
		proposedPosition (Point): The proposed position

	Returns:
		Boolean: TRUE if the position is on the platform, FALSE otherwise
	------------------------------------------
	"""
	def testIfWithinBoundaries(self, proposedPosition):
		return self.origin.__le__(proposedPosition) and self.rightUpperCorner.__ge__(proposedPosition)
   
