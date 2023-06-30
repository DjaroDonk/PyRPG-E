import pygame
from game import Game
from renderer import *
import colors
from world import *
from player import *

pygame.init()

game = Game()

game.setScreenSize((1200,800))
screen = pygame.display.set_mode(game.screenSize, pygame.RESIZABLE)
game.setScreen(screen)

world = World((12,8))
render_Wall = RenderObject()
render_Wall.setColor(colors.black)
render_Wall.setShape("square")
prefab_Wall = WorldObject()
prefab_Wall.name = "wall"
prefab_Wall.renderObject = render_Wall

render_Coin = RenderObject()
render_Coin.setColor(colors.yellow)
render_Coin.setShape("circle")
render_Coin.setScale(0.4)
prefab_Coin = WorldObject()
prefab_Coin.name = "coin"
prefab_Coin.renderObject = render_Coin

render_Player = RenderObject()
render_Player.setColor(colors.lightBlue)
render_Player.setShape("circle")
render_Player.setScale(0.7)

player = Player()
player.setPosition([0,2])
player.setRenderObject(render_Player)
player.setWorld(world)
game.setPlayer(player)
player.addBlocker("wall")
player.setSpeed(30)

world.setObject((0,0), prefab_Wall)
world.setObject((2,1), prefab_Wall)
world.setObject((2,2), prefab_Coin)
game.setWorld(world)

game.setRenderer(defaultRenderer)
defaultRenderer.backgroundSquares = True
game.renderer.setBackgroundColor(colors.white)
game.start()
clock = pygame.time.Clock()
clock.tick()

while game.running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.quit()
            elif event.key == pygame.K_DOWN:
                player.parseEvent(["move","down",True])
            elif event.key == pygame.K_UP:
                player.parseEvent(["move","up",True])
            elif event.key == pygame.K_LEFT:
                player.parseEvent(["move","left",True])
            elif event.key == pygame.K_RIGHT:
                player.parseEvent(["move","right",True])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.parseEvent(["drop","down"])
            elif event.key == pygame.K_UP:
                player.parseEvent(["drop","up"])
            elif event.key == pygame.K_RIGHT:
                player.parseEvent(["drop","right"])
            elif event.key == pygame.K_LEFT:
                player.parseEvent(["drop","left"])
    game.player.update(dt)
    game.render()
    pygame.display.flip()