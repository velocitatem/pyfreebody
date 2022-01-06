from random import randint
from PIL import Image, ImageDraw, ImageFont
import math
from datetime import datetime

def freebody(schema):

    img  = Image.new( mode = "RGB", size = (size, size), color = (225,225,225))
    canvas = ImageDraw.Draw(img)

    mean = 0
    for force in schema['forces']:
        mean+=force['magnitude']
    mean /= len(schema['forces'])
    print(mean)
    i=0

    for force in schema['forces']:
        color = randomColor()
        force['prop'] = mean / force['magnitude']
        CreatArrow(canvas, force, color)
        ForceLegend(canvas, force, i, color)

        i+=1

    canvas.rectangle(((center*0.8, center*0.8), (center*1.2, center*1.2)), outline = black, fill = black)

    now = datetime.now()
    dtstr = now.strftime("%d-%m-%Y %H:%M:%S")
    path = "pyfreebody-"+schema['name']+".png"
    img.save(path)
    return path
#    img.show()

size = 600
arrowHeadSize = 15
cw = 400 * 0.1
center = size / 2;
rectW = size * 0.4

black = (0,0,0)
font = ImageFont.truetype("/usr/share/fonts/noto/NotoSans-Regular.ttf", 20)

def randomColor():
    return (randint(0, 255),
          randint(0, 255),
          randint(0, 255))

def ArrowCordinates(force):
    theta = force['theta']
    m = force['prop'] * 150
    yc = m * math.sin(theta)
    xc = m * math.cos(theta)
    return ((center, center), (center+ xc, center - yc))

def ArrowHeadCordinates(arrowCords):
    x, y = arrowCords[1][0], arrowCords[1][1]
    dx = arrowHeadSize * math.cos(math.pi/8)
    dy = (2 * arrowHeadSize * math.sin(math.pi/8))/2
    return (
        (x-dx, y + dy),
        (x+dx, y - dy),
        (x-dx, y + dy)
    )
def ForceLegend(canvas, force, i, color):
    text = force['name'] + " = " + str(force['magnitude']) + "N"
    canvas.text((5,5+i*20), text, fill = color, font = font)

def CreatArrow(canvas, force, color):
    arrowBase = ArrowCordinates(force)
    canvas.line(arrowBase, width=10, fill = color)
    canvas.polygon(ArrowHeadCordinates(arrowBase), fill = color)




