#!/usr/bin/env python3
from pyfreebody import Freebody, Direction

body = Freebody("test1", 30) # name, mass

body.addForce("Normal", 300, Direction.up) # name, magnitude, theta
body.addForce("Friction", 4, Direction.left) # name, magnitude, theta

body.diagram() # creates the diagram
