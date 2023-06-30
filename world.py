from worldObjects import *

class World():
    def __init__(self, size):
        self.size = size
        self.world = []
        for x in range(size[0]):
            self.world.append([])
            for y in range(size[1]):
                self.world[x].append(empty_Object)
    def setObject(self, position, prefab):
        newObject = WorldObject()
        newObject.position = position
        newObject.name = prefab.name
        newObject.renderObject = prefab.renderObject
        self.world[position[0]][position[1]] = newObject
    def getSize(self):
        return self.size
    def update(self):
        pass
        