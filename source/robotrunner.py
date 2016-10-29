from .myPlatform import myPlatform
from .robot import robot
from .direction import Direction
from .point import Point
from re import compile,X
from sys import exit,argv

def main(file):
	pattern = compile(r"""(?<=^)                                    # start
						(?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
						(?=\s?                                    # space
						(?P<x>\d+),                               # x co-ord
						(?P<y>\d+),                               # y co-ord
						(?P<dir>NORTH|EAST|SOUTH|WEST)            # direction
						$))                                       # EOL
						""", X)

	p = myPlatform(Point(0,0), Point(5,5))
	r = robot(p)

	with open(file) as f:
		for line in f:
			m = pattern.match(line.rstrip('\n'))
			if m is not None and m.group("cmd") == "PLACE":
				r = r.PLACE(p,Point(int(m.group("x")),int(m.group("y"))),Direction(m.group("dir")))
     
			elif m is not None and hasattr(r,m.group("cmd")):
				r = getattr(r,m.group("cmd"))()

    
