class Game():
    def __init__(self):
        self.world = None
        self.running = False
        self.screen = None
        self.renderer = None
        self.screenSize = (500,500)
        self.player = None
    def quit(self):
        self.running = False
    def start(self):
        self.running = True
    def setScreen(self, screen):
        self.screen = screen
    def setRenderer(self, renderer):
        self.renderer = renderer
    def render(self):
        self.renderer.render(self.screen, self.world, self.player)
    def setScreenSize(self, size):
        self.screenSize = size
    def setWorld(self, world):
        self.world = world
    def setPlayer(self, player):
        self.player = player