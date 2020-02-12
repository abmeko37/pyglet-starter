import pyglet
from pyglet.window import key
window = pyglet.window.Window()



image = pyglet.image.load('assets/hero/sliced/idle-1.png')
cavimg = pyglet.image.load('assets/forest-assets/cave.png')
floor = pyglet.image.load('assets/forest-assets/floor.png')
stairs= pyglet.image.load('assets/forest-assets/stairs.png')
door = pyglet.image.load('assets/forest-assets/door.png')
label = pyglet.text.Label( 'how is {bold True}it going', 
                        font_name = 'italics',
                        font_size =36,
                        x=window.width//2, y=window.height//2,
                        anchor_x=('center'),anchor_y=('center'))


keys = key.KeyStateHandler()
window.push_handlers(keys)
def update (dt):
    pass

@window.event
def on_draw():
    window.clear()
    image.blit(100,150)
    cavimg.blit(200,250)
    floor.blit(300,200)
    stairs.blit(400,100)
    if keys[key.RIGHT]:
        stairs.blit(400,100)
    door.blit(500,100)

    if keys[key.SPACE]:
        label.draw()

    
    
  


pyglet.app.run()
