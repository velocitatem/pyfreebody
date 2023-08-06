from pyfreebody.pyfreebody import Freebody, Direction, SystemType, blueColor, LegendType
import math

sysinc = math.pi/4
body = Freebody("inclinedplane", 20, SystemType.inclinedPlane, sysinc,
color=blueColor, legend=LegendType.arrow)
body.addForce("Normal", 200, sysinc + math.pi/2)
body.diagram()
