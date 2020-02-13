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
spr = pyglet.sprite.Sprite(door,x=0, y=200)
 


keys = pyglet.window.key.KeyStateHandler()

def update (dt):
   window.push_handlers(keys)
   if keys[pyglet.window.key.UP]:
        spr.x +=1
    

        

@window.event
def on_draw():
    window.clear()
    
    image.blit(100,150)
    cavimg.blit(200,250)
    floor.blit(300,200)
    stairs.blit(400,100)

    door.blit(500,100)
    spr.draw()
    
    if keys[key.SPACE]:
        label.draw()
        print("spacebar pressed!")

    
    
  

pyglet.clock.schedule(update)
pyglet.app.run()
