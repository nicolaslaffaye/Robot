"""
    ------------------------------------------
The class myPlatform implements the object platform and its command
A platform has four attributes:
    Args:
        originePosX (int): The origin on X axis for the platform.
        originePosX (int): The origin on Y axis for the platform.
        maxPosX (int): The extreme position of the platform on the X axis.
        maxPosY(int): The extreme position of the platform on the Y axis..

    ------------------------------------------
"""
class myPlatform:

    def __init__(self, originePosX, originePosY, maxPosX, maxPosY):
        self.maxPosX = maxPosX                                      #value imposed for this exercice
        self.maxPosY = maxPosY                                      #value imposed for this exercice
        self.originePosX = originePosX                              #value imposed for this exercice
        self.originePosY = originePosY                              #value imposed for this exercice

    """
    ------------------------------------------
    testIfWithinBoundaries is the function checking if a position in on the platform
    Args:
        x (int): The position on the X axis.
        y (int): The position on the Y axis.

    Returns:
        Boolean: TRUE if the position is on the platform, FALSE otherwise
    ------------------------------------------
    """
    def testIfWithinBoundaries(self,x,y):
        if x > self.maxPosX or x<self.originePosX or y>self.maxPosY or y<self.originePosY:
            return False
        else:
            return True
