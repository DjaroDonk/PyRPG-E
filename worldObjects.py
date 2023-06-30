class RenderObject():
    def __init__(self):
        self.color = (0,0,0)
        self.shape = "square"
        self.scale = 1
        self.invisible = False
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setShape(self, shape):
        self.shape = shape
    def getShape(self):
        return self.shape
    def getScale(self):
        return self.scale
    def setScale(self, scale):
        self.scale = scale
    

class WorldObject():
    def __init__(self):
        self.name = None
        self.position = None
        self.renderObject = None

empty_Render = RenderObject()
empty_Render.invisible = True
empty_Object = WorldObject()
empty_Object.renderObject = empty_Render
empty_Object.name = "None"