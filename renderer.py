import pygame

class Renderer():
    def __init__(self):
        self.backgroundColor = (255,255,0)
        self.backgroundSquares = False
        self.backgroundSquaresColor = (200,200,200)
    def setBackgroundColor(self, color):
        self.backgroundColor = color
    def renderObject(self, screen, renderObject, position, scale):
        if renderObject.invisible:
            return
        x = position[0]
        y = position[1]
        if renderObject.shape == "square":
            spriteToDraw = pygame.Rect(x*scale, y*scale, scale, scale)
            pygame.draw.rect(screen, renderObject.getColor(), spriteToDraw)
        elif renderObject.shape == "circle":
            pygame.draw.circle(screen, renderObject.getColor(), (x*scale+scale/2, y*scale+scale/2), renderObject.scale * scale/2)
    def render(self, screen, world, player):
        screenSize = screen.get_size()
        worldSize = world.getSize()
        maxSizeX = screenSize[0] // worldSize[0]
        maxSizeY = screenSize[1] // worldSize[1]
        if maxSizeX <= maxSizeY:
            scale = maxSizeX
        else:
            scale = maxSizeY
        screen.fill((0,0,0))
        pygame.draw.rect(screen, self.backgroundColor, pygame.Rect(0,0,scale*worldSize[0],scale*worldSize[1]))
        for x in range(world.getSize()[0]):
            for y in range(world.getSize()[1]):
                if self.backgroundSquares:
                    pygame.draw.rect(screen, self.backgroundSquaresColor, pygame.Rect(x*scale,y*scale,scale,scale))
                    pygame.draw.rect(screen, self.backgroundColor, pygame.Rect(x*scale+2,y*scale+2,scale-4,scale-4))
                objectToDraw = world.world[x][y]
                if objectToDraw != None:
                    self.renderObject(screen, objectToDraw.renderObject, (x,y), scale)
        
        self.renderObject(screen, player.renderObject, player.position, scale)
                    

defaultRenderer = Renderer()