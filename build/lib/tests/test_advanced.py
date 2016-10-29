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

        p = source.myPlatform(source.Point(0,0),source.Point(5,5))          #Create a new myPlatform P with origin (0,0) and 5 long on both X and Y axis
        r = source.robot(p)                     	                    #Create a new robot which is placed on myPlatform p
        
        """Test the no initial placement"""
        r = r.MOVE()                                                        #Expect ignore command
        r = r.REPORT()                                                          #Expect ignore command
        r = r.LEFT()                                                        #Expect ignore command
        r = r.RIGHT()                                                       #Expect ignore command
        r = r.PLACE(p, source.Point(0,0), source.Direction("NORTH"))
        
        """Test 1 as per instruction"""
        print("test1")
        r = r.PLACE(p, source.Point(0,0), source.Direction("NORTH"))
        r = r.MOVE()
        r = r.REPORT()                                                          #Expect (0,1,NORTH)
        
        """Test 2 as per instruction"""
        print("test2")
        r = r.PLACE(p, source.Point(0,0), source.Direction("NORTH"))
        r = r.LEFT()
        r = r.REPORT()                                                          #Expect (0,0,WEST)
        
        """Test 3 as per instruction"""
        print("test3")
        r = r.PLACE(p, source.Point(1,2), source.Direction("EAST"))
        r = r.MOVE()
        r = r.MOVE()
        r = r.LEFT()
        r = r.MOVE()
        r = r.REPORT()                                                          #Expect (3,3,NORTH)

        """Test incorect instruction"""
        print("test4")
        r = r.PLACE(p, source.Point(0,0),source.Direction("yeew"))          #Expect error message placement incorrect
        r = r.MOVE()
        r = r.REPORT()                                                          #Expect (3,4,NORTH) 

        """test out of Boundaries from PLACE"""
        print("test5")
        r = r.PLACE(p, source.Point(-1,0),source.Direction("WEST"))         #Expect error message not on the platform
        r = r.PLACE(p, source.Point(0,-1),source.Direction("WEST"))         #Expect error message not on the platform
        r = r.PLACE(p, source.Point(6,2),source.Direction("WEST"))          #Expect error message not on the platform
        r = r.PLACE(p, source.Point(2,6),source.Direction("WEST"))          #Expect error message not on the platform

        """Test out of Boundaries Movement leading for robot to fall"""
        print("test6")
        r = r.PLACE(p, source.Point(5,5),source.Direction("NORTH"))
        r = r.MOVE()                                                        #Expect error message this move would lead to a damage
        r = r.REPORT()                                                          #Expect (5,5,NORTH)
        r = r.PLACE(p, source.Point(0,4),source.Direction("WEST"))
        r = r.MOVE()                                                        #Expect error message this move would lead to a damage
        r = r.MOVE()                                                        #Expect error message this move would lead to a damage
        r = r.REPORT()                                                          #Expect (0,4,WEST)
        r = r.RIGHT()
        r = r.MOVE()
        r = r.MOVE()                                                        #Expect error message this move would lead to a damage
        r = r.REPORT()                                                          #Expect (0,5,NORTH)
        

if __name__ == '__main__':
    unittest.main()
