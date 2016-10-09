"""
    ------------------------------------------
The class robot implements the object robot and its command
A robot has only one attribute which is the platform it is placed on
A robot responds to the following commands:
PLACE, MOVE, LEFT, RIGHT and REPORT
    ------------------------------------------
"""

class robot:

    robotInitiallyPlaced = False                                                #Boolean assesing whether the robot has been placed on a platform (TRUE) or not (FALSE)
    
    def __init__(self, support):
        self.posX = 0                                                           #Integer representing the robot position on the X axis. Robot initially at origin (0,0)
        self.posY = 0                                                           #Integer representing the robot position on the Y axis. Robot initially at origin (0,0)
        self.orientation = ""                                                   #String representing the robot orientation WEST, EAST, NORTH or SOUTH
        self.support = support                                                  #MyPlatform object representing the platform the robot has been placed on


    """
    ------------------------------------------
    PLACE is the function placing the robot on the platform
    Args:
        x (int): The position on the X axis.
        y (int): The position on the Y axis.
        F (str): The orientation WEST, EAST, NORTH or SOUTH.

    Returns:
        NIL
    ------------------------------------------
    """
    def PLACE(self, x, y, F):

        self.robotInitiallyPlaced = True                                        #The robot has now been placed on the platform
        if self.support.testIfWithinBoundaries(x, y):                           #Using the platform function to test if the placement would be valid.
            self.posX = x                                                       #Set the robot attribute posX accordingly
            self.posY = y                                                       #Set the robot attribute posY accordingly
            if F == "SOUTH" or F == "NORTH" or F == "EAST" or F == "WEST":      #If the orientation given is correct
                self.orientation = F                                            #Set the robot attribute orientation accordingly
            else:
                print ("please replace the robot with a correct orientation (EAST, WEST, SOUTH or NORTH)")
        else:
            print("Please place the robot within the platform boundaries")



    """
    ------------------------------------------
    MOVE is the function moving the robot on the platform
    It increases the X or Y axis position by 1 depending on the orientation
    
    Args:
        NONE

    Returns:
        NIL
    ------------------------------------------
    """
    def MOVE(self):
        if self.robotInitiallyPlaced:                                           #If the robot was previously positioned on a platform
            (__posX, __posY) = self.__calculateNextPosition()                   #Calculate what would be the next position
            if self.support.testIfWithinBoundaries(__posX, __posY):             #Check if the next position is inside the platform
                self.posX = __posX                                              #Set robot attribute posX to the new position
                self.posY = __posY                                              #Set robot attribute posY to the new position
            else:
                print("Movement canceled in order to prevent damages")
        else:
            print("Please place the robot first using PLACE(x,y,Orientation)")


    """
    ------------------------------------------
    LEFT is the function rotating the robot 90 degrees on the left
    
    Args:
        NONE

    Returns:
        NIL
    ------------------------------------------
    """
    def LEFT(self):
        if self.robotInitiallyPlaced:                                           #If the robot was previously positioned on a platform
            if self.orientation == "NORTH":
                self.orientation = "WEST"
            elif self.orientation == "SOUTH":
                self.orientation = "WEST"
            elif self.orientation == "WEST":
                self.orientation = "SOUTH"
            elif self.orientation == "EAST":
                self.orientation = "NORTH"
            else:
                print ("please replace the robot with a correct orientation")
        else:
            print("Please place the robot first using PLACE(x,y,Orientation)")


    """
    ------------------------------------------
    RIGHT is the function rotating the robot 90 degrees on the right
    
    Args:
        NONE

    Returns:
        NIL
    ------------------------------------------
    """
    def RIGHT(self):
        if self.robotInitiallyPlaced:                                           #If the robot was previously positioned on a platform
            if self.orientation == "NORTH":
                self.orientation = "EAST"
            elif self.orientation == "SOUTH":
                self.orientation = "EAST"
            elif self.orientation == "WEST":
                self.orientation = "NORTH"
            elif self.orientation == "EAST":
                self.orientation = "SOUTH"
            else:
                print ("please replace the robot with a correct orientation")
        else:
            print("Please place the robot first using PLACE(x,y,Orientation)")


    """
    ------------------------------------------
    REPORT is the function outputing the robot current position and orientation
    
    Args:
        NONE

    Returns:
        NIL
    ------------------------------------------
    """
    def REPORT(self):
        if self.robotInitiallyPlaced:                                           #If the robot was previously positioned on a platform
            print(self.posX,self.posY,self.orientation)
        else:
            print("Please place the robot first using PLACE(x,y,Orientation)")

    """
    ------------------------------------------
    __calculateNextPosition is the private function calculating the futur robot position
    
    Args:
        NONE

    Returns:
        __posX (int): The futur position on the X axis.
        __posY (int): The futur position on the Y axis.
    ------------------------------------------
    """
    def __calculateNextPosition(self):
        __posX = self.posX                                                      #Set __posX to the current robot position on X axis
        __posY = self.posY                                                      #Set __posY to the current robot position on Y axis
        if self.orientation == "NORTH": 
            __posY = self.posY + 1                                              #Set __posX or __posY to the futur robot position on the axis
        elif self.orientation == "SOUTH": 
            __posY = self.posY - 1
        elif self.orientation == "WEST": 
            __posX = self.posX - 1
        elif self.orientation == "EAST":
            __posX = self.posX + 1
        else:
            print ("please replace the robot with a correct orientation") 
        return  __posX, __posY
