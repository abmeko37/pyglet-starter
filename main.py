import pygame
import pyglet
window = pyglet.window.Window()
def update (dt):
    pass



image = pyglet.image.load('assets/hero/sliced/idle-1.png')
cavimg = pyglet.image.load('assets/forest-assets/cave.png')
floor = pyglet.image.load('assets/forest-assets/floor.png')
stairs= pyglet.image.load('assets/forest-assets/stairs.png')
door = pyglet.image.load('assets/forest-assets/door.png')
font = pygame.font.SysFont("arial", 72)

text = font.render("Hello, World", True, (0, 128, 0))



@window.event
def on_draw():
    window.clear()
    image.blit(100,150)
    cavimg.blit(200,250)
    floor.blit(300,200)
    stairs.blit(400,100)
    door.blit(500,100)
    win.blit(text, (400, 300))
    
  


pyglet.app.run()
