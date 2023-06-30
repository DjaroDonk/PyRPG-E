import pygame

class Player():
    def __init__(self):
        self.position = [0,0]
        self.targetPosition = [0,0]
        self.renderer = None
        self.world = None
        self.blockers = []
        self.moving = False
        self.movingDirection = "none"
        self.movementSpeed = 1
        self.backlogMove = "none"
        self.directionsHeld = []
        self.oneTap = False
    def setSpeed(self, speed):
        self.movementSpeed = speed
    def setPosition(self, position):
        self.position = position.copy()
        self.targetPosition = position.copy()
    def addBlocker(self, name):
        self.blockers.append(name)
    def setWorld(self, world):
        self.world = world
    def getPosition(self):
        return self.position
    def setRenderObject(self, renderObject):
        self.renderObject = renderObject
    def parseEvent(self, key):
        x = self.position[0]
        y = self.position[1]
        max = self.world.getSize()
        if key[0] == "move":
            if key[2]:
                self.oneTap = True
            if self.moving:
                if key[2]:
                    if not key[1] in self.directionsHeld:
                        self.directionsHeld.append(key[1])
                if self.movingDirection != key[1]:
                    self.backlogMove = key[1]
                return
            if key[1] == "down":
                if key[2] and not "down" in self.directionsHeld:
                    self.directionsHeld.append("down")
                if y + 1 >= max[1]:
                    pass
                elif self.world.world[x][y+1].name in self.blockers:
                    pass
                else:
                    self.targetPosition[1] += 1
                    self.moving = True
                    self.movingDirection = "down"
            elif key[1] == "up":
                if key[2] and not "up" in self.directionsHeld:
                    self.directionsHeld.append("up")
                if y - 1 < 0:
                    pass
                elif self.world.world[x][y-1].name in self.blockers:
                    pass
                else:
                    self.targetPosition[1] -= 1
                    self.moving = True
                    self.movingDirection = "up"
            elif key[1] == "right":
                if key[2] and not "right" in self.directionsHeld:
                    self.directionsHeld.append("right")
                if x + 1 >= max[0]:
                    pass
                elif self.world.world[x+1][y].name in self.blockers:
                    pass
                else:
                    self.targetPosition[0] += 1
                    self.moving = True
                    self.movingDirection = "right"
            elif key[1] == "left":
                if key[2] and not "left" in self.directionsHeld:
                    self.directionsHeld.append("left")
                if x - 1 < 0:
                    pass
                elif self.world.world[x-1][y].name in self.blockers:
                    pass
                else:
                    self.targetPosition[0] -= 1
                    self.moving = True
                    self.movingDirection = "left"
        elif key[0] == "drop":
            if key[1] == "down":
                if "down" in self.directionsHeld:
                    self.directionsHeld.remove("down")
                if self.moving and self.movingDirection == "down" and not self.oneTap:
                    if self.targetPosition[1] - self.position[1] > 0.8:
                        self.targetPosition[1] = int(self.position[1])
                        self.movingDirection = "up"
            elif key[1] == "up":
                if "up" in self.directionsHeld:
                    self.directionsHeld.remove("up")
                if self.moving and self.movingDirection == "up" and not self.oneTap:
                    if self.position[1] - self.targetPosition[1] > 0.8:
                        self.targetPosition[1] = int(self.position[1]) + 1
                        self.movingDirection = "down"
            elif key[1] == "right":
                if "right" in self.directionsHeld:
                    self.directionsHeld.remove("right")
                if self.moving and self.movingDirection == "right" and not self.oneTap:
                    if self.targetPosition[0] - self.position[0] > 0.8:
                        self.targetPosition[0] = int(self.position[0])
                        self.movingDirection = "left"
            elif key[1] == "left":
                if "left" in self.directionsHeld:
                    self.directionsHeld.remove("left")
                if self.moving and self.movingDirection == "left" and not self.oneTap:
                    if self.position[0] - self.targetPosition[0] > 0.8:
                        self.targetPosition[0] = int(self.position[0]) + 1
                        self.movingDirection = "right"
    def afterMove(self):
        #print(self.directionsHeld)
        self.oneTap = False
        if len(self.directionsHeld) > 0:
            self.parseEvent(["move",self.directionsHeld[-1],False])
        elif self.backlogMove != "none":
            self.parseEvent(["move",self.backlogMove,False])
            self.backlogMove = "none"
    def update(self, dt):
        if self.moving:
            if self.movingDirection == "down":
                self.position[1] += 0.1 * dt * self.movementSpeed 
                if self.position[1] >= self.targetPosition[1]:
                    self.position[1] = self.targetPosition[1]
                    self.moving = False
                    self.movingDirection = "none"
                    self.afterMove()
            elif self.movingDirection == "up":
                self.position[1] -= 0.1 * dt * self.movementSpeed
                if self.position[1] <= self.targetPosition[1]:
                    self.position[1] = self.targetPosition[1]
                    self.moving = False
                    self.movingDirection = "none"
                    self.afterMove()
            elif self.movingDirection == "right":
                self.position[0] += 0.1 * dt * self.movementSpeed 
                if self.position[0] >= self.targetPosition[0]:
                    self.position[0] = self.targetPosition[0]
                    self.moving = False
                    self.movingDirection = "none"
                    self.afterMove()
            elif self.movingDirection == "left":
                self.position[0] -= 0.1 * dt * self.movementSpeed
                if self.position[0] <= self.targetPosition[0]:
                    self.position[0] = self.targetPosition[0]
                    self.moving = False
                    self.movingDirection = "none"
                    self.afterMove()
        