# -*- coding: utf-8 -*-

from context import source

import unittest


class AdvancedTestSuite(unittest.TestCase):

    """
    ------------------------------------------
    test_case implements all the tests required in order to validate our class robot
    
    Args:
        NONE

    Returns:
        NIL
    -------
    """
    def test_case(self):

        p = source.myPlatform(0,0,5,5)          #Create a new myPlatform P with origin (0,0) and 5 long on both X and Y axis
        r = source.robot(p)                     #Create a new robot which is placed on myPlatform p
        
        """Test the no initial placement"""
        r.MOVE()                                #Expect ignore command
        r.REPORT()                              #Expect ignore command
        r.LEFT()                                #Expect ignore command
        r.RIGHT()                               #Expect ignore command
        r.PLACE(0,0, "NORTH")
        
        """Test 1 as per instruction"""
        r.PLACE(0,0, "NORTH")
        r.MOVE()
        r.REPORT()                              #Expect (0,1,NORTH)
        
        """Test 2 as per instruction"""
        r.PLACE(0,0, "NORTH")
        r.LEFT()
        r.REPORT()                              #Expect (0,0,WEST)
        
        """Test 3 as per instruction"""
        r.PLACE(1,2, "EAST")
        r.MOVE()
        r.MOVE()
        r.LEFT()
        r.MOVE()
        r.REPORT()                              #Expect (3,3,NORTH)

        """Test incorect instruction"""
        r.PLACE(0,0,"yeew")                     #Expect error message placement incorrect
        r.MOVE()
        r.REPORT()                              #Expect (0,1,NORTH) (only the orientation command should be ignored from the last PLACE)

        """test out of Boundaries from PLACE"""
        r.PLACE(-1,0,"WEST")                    #Expect error message not on the platform
        r.PLACE(0,-1,"WEST")                    #Expect error message not on the platform
        r.PLACE(6,2,"WEST")                     #Expect error message not on the platform
        r.PLACE(2,6,"WEST")                     #Expect error message not on the platform

        """Test out of Boundaries Movement leading for robot to fall"""
        r.PLACE(5,5,"NORTH")
        r.MOVE()                                #Expect error message this move would lead to a damage
        r.REPORT()                              #Expect (5,5,NORTH)
        r.PLACE(0,4,"WEST")
        r.MOVE()                                #Expect error message this move would lead to a damage
        r.MOVE()                                #Expect error message this move would lead to a damage
        r.REPORT()                              #Expect (0,4,WEST)
        r.RIGHT()
        r.MOVE()
        r.MOVE()                                #Expect error message this move would lead to a damage
        r.REPORT()                              #Expect (0,5,NORTH)
        

if __name__ == '__main__':
    unittest.main()
