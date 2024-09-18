from random import randint
from PIL import Image, ImageDraw, ImageFont
import math
from datetime import datetime
from enum import Enum
import os

class SystemType(Enum):
    basic = 0
    inclinedPlane = 1

class System:
    def __init__(self, sysType=SystemType.basic, incline:float=0):
        self.sysType = sysType
        self.incline = incline

class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        self.forces = []

class Force:
    def __init__(self, name, magnitude, theta, units="N"):
        self.name = name
        self.magnitude = magnitude
        self.theta = theta
        self.units = units

class Direction(Enum):
    up = math.pi /2
    down = (3 * math.pi) / 2
    left = math.pi
    right = 0

class LegendType(Enum):
    default = 0 # text on top left
    arrow = 1   # text and number with arrow

def randomColor():
    return (randint(0, 180),
          randint(0, 180),
          randint(0, 180))

def blackColor():
    return black

def blueColor():
    return (0, 20, 200)

class Freebody:

    def __init__ (self, name="empty", mass=24, sysType = SystemType.basic, incline=math.pi/6, arrows=False,
                  color=randomColor, legend=LegendType.default, path=None):
        body = Body(name, mass)
        self.system = System(sysType, incline)
        self.body = body
        self.arrows = arrows
        self.color_fn = color
        self.legend = legend
        self.path = path

    def addForce(self, name, magnitude, theta):
        v = theta
        if type(v) == Direction:
            v = theta.value
        self.body.forces.append(Force(name, magnitude, v))


    def diagram(self):

        img  = Image.new( mode = "RGB", size = (size, size), color = (255,255,255))
        canvas = ImageDraw.Draw(img)
        sm = 0
        for force in self.body.forces:
            sm += force.magnitude


        if(self.system.sysType == SystemType.basic):

            canvas.rectangle(((center*0.8, center*0.8), (center*1.2, center*1.2)),
                             outline = black)

            canvas.ellipse(((center*0.96, center*0.96), (center*1.04, center*1.04)),
                           outline = black, fill = black)


        #    img.show()
        #
        # BROKEN FOR THETA  >= PI/5
        #
        elif(self.system.sysType == SystemType.inclinedPlane):

            theta = self.system.incline
            theta = math.pi/2 - theta
            rvw = center * 0.4
            inclineoffy = rvw/2/abs(math.sin(theta)) if theta % (math.pi/2) != 0 else 0 # catch vertical inclined planed
            inclineoffx = 0 if theta % (math.pi/2) != 0 else rvw/2

            vertices = makeRectangle(rvw, rvw, theta, offset=(center, center))
            verticesPlane = makeRectangle(3, size*1.2, theta, offset=(center-inclineoffx, center+inclineoffy))

            canvas.polygon(vertices, fill=white, outline = black)
            canvas.polygon(verticesPlane, fill = 0)

        def get_text_dimensions(text_string, font):
            # https://stackoverflow.com/a/46220683/9263761
            ascent, descent = font.getmetrics()

            text_width = font.getmask(text_string).getbbox()[2]
            text_height = font.getmask(text_string).getbbox()[3] + descent

            return (text_width, text_height)
        try:
            masstxt = self.body.mass.title()
        except AttributeError:
            masstxt = str(self.body.mass) + "kg"
        mtsw, mtsh = get_text_dimensions(masstxt, font)
        canvas.text((center - (mtsw / 2), center + (mtsh / 2)), masstxt, fill=black, font=font)

        if self.body.name != "":
            canvas.text((10,size-30), str(self.body.name), fill = black)


        i=0
        print(self.body.forces)
        for force in self.body.forces:
            color = self.color_fn()
            force.prop =  force.magnitude / sm
            print(force.prop)
            CreatArrow(canvas, force, color, arrow=self.arrows, label=self.legend)
            if self.legend == LegendType.default:
                ForceLegend(canvas, force, i, color)
            i+=1

        if self.path is not None:
            path = self.path
        else:
            now = datetime.now()
            dtstr = now.strftime("%d-%m-%Y %H:%M:%S")
            path = "pyfreebody-"+self.body.name+".png"
        img.save(path)
        # try to open the image
        try:
            img.show()
        except:
            print("Image saved to: "+path)

        return path


size = 600
arrowHeadSize = 15
cw = 400 * 0.1
center = size / 2;
rectW = size * 0.4

black = (0,0,0)
white = (225,225,225)


try:
    font = ImageFont.truetype("arial.ttf", 20)
    fontTag = ImageFont.truetype("arial.ttf", 12)
except IOError:
    font = ImageFont.load_default()
    fontTag = ImageFont.load_default()


# home = os.path.dirname(os.path.abspath(__file__)) #<-- absolute dir the script is in
# font = ImageFont.truetype(home+"/pyfreebody.ttf", 20)
# fontTag = ImageFont.truetype(home+"/pyfreebody.ttf", 12)

def makeRectangle(l, w, theta, offset=(0,0)):
    c, s = math.cos(theta), math.sin(theta)
    rectCoords = [(l/2.0, w/2.0), (l/2.0, -w/2.0), (-l/2.0, -w/2.0), (-l/2.0, w/2.0)]
    return [(c*x-s*y+offset[0], s*x+c*y+offset[1]) for (x,y) in rectCoords]


def ArrowCordinates(force):
    theta = force.theta
    m = force.prop * 100
    # m+=rectW/2
    xrc = rectW/4 * math.cos(theta)
    yrc = rectW/4 * math.sin(theta)
    yc = m * math.sin(theta)
    xc = m * math.cos(theta)
    return ((center+xrc, center-yrc), (center+xrc+xc, center-yrc - yc))


def tagCordinates(arrowCords):
    tip_x, tip_y = arrowCords[1][0], arrowCords[1][1]
    try:
        theta = math.atan((tip_y-center)/(tip_x-center))
    except ZeroDivisionError:
        theta = math.pi/2 if tip_y > center else -math.pi/2
    if tip_y == center and tip_x < center:
        theta = math.pi
    dx = arrowHeadSize * math.cos(theta)
    dy = arrowHeadSize * math.sin(theta)
    return (tip_x+dx, tip_y+dy)

def tagAlign(theta):
    theta = theta % (2*math.pi)
    if theta < math.pi/8:
        return "lm"
    elif theta < math.pi/3:
        return "ld" # 'b'ottom and 't'op codes don't work with multiline, use 'd'escender and 'a'scender instead
    elif theta < 2*math.pi/3:
        return "md"
    elif theta < (9./8) * math.pi:
        return "rm"
    elif theta < (4./3)*math.pi:
        return "ra"
    elif theta < (5./3)*math.pi:
        return "ma"
    else:
        return "lm"

def ArrowHeadCordinates(arrow):
    arrow_x, arrow_y = arrow[1][0] - arrow[0][0], arrow[1][1] - arrow[0][1]
    arrow_len = math.sqrt(arrow_x * arrow_x + arrow_y * arrow_y)
    arrow_unit_v = (arrow_x/arrow_len, arrow_y/arrow_len)
    dx, dy = arrow_unit_v[0] * arrowHeadSize, arrow_unit_v[1] * arrowHeadSize
    tip_x, tip_y = arrow[1][0], arrow[1][1]
#    print(dx, dy)
#    print(tip_x, tip_y)
    return (
        (tip_x+dx, tip_y + dy), # arrow tip
        (tip_x-dy, tip_y + dx),
        (tip_x+dy, tip_y - dx)
    )

def ForceLegend(canvas, force, i, color):
    text = f"{force.name}  Force =  {str(force.magnitude)} {force.units}"
    canvas.text((5,5+i*20), text, fill = color, font = font)

def CreatArrow(canvas, force, color, arrow=True, label = LegendType.default):
    arrowBase = ArrowCordinates(force)
    canvas.line(arrowBase, width=10, fill = color)
    ltext =f"F{force.name[0:1].lower()}" if label == LegendType.default else f"{force.name}\n{str(force.magnitude)} {force.units}"
    arrow_font = fontTag if label == LegendType.default else font
    canvas.text(tagCordinates(arrowBase), ltext, font=arrow_font, fill = black, anchor=tagAlign(force.theta))
    if arrow:
        canvas.polygon(ArrowHeadCordinates(arrowBase), fill = color)
