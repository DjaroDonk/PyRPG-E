import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
purple = (255,0,255)
cyan = (0,255,255)
lightBlue = (128,128,255)
lightGreen = (128,255,128)
lightRed = (255,128,128)
lightYellow = (255,255,128)
pink = (255,128,255)
lightCyan = (128,255,255)

allColors = [black,white,red,green,blue,yellow,purple,cyan,lightBlue,lightGreen,lightRed,lightYellow,pink,lightCyan]
def randomColor():
    return random.choice(allColors)