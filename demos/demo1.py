from pyfreebody.pyfreebody import Freebody, Direction, SystemType
import math

sysinc = math.pi/4
body = Freebody("inclinedplane", 20, SystemType.inclinedPlane, sysinc)
body.addForce("Normal", 200, sysinc + math.pi/2)
body.diagram()
