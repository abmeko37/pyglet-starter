import pyglet
from pyglet.window import key

life = 10
window = pyglet.window.Window()



image = pyglet.image.load('assets/hero/Old hero.png')
cavimg = pyglet.image.load('assets/forest-assets/cave.png')
cavesmal = cavimg.get_region(x=20, y=10, width = 32, height = 32)

floor = pyglet.image.load('assets/forest-assets/floor.png')
stairs= pyglet.image.load('assets/forest-assets/stairs.png')
door = pyglet.image.load('assets/forest-assets/door.png')
label = pyglet.text.Label( 'GAME OVer', 
                        font_name = 'italics',
                        font_size =36,
                        x=window.width//2, y=window.height//2,
                        anchor_x=('center'),anchor_y=('center'))

smolimg = image.get_region(x=10, y=10, width = 32, height = 32)
spr = pyglet.sprite.Sprite(smolimg,x=0, y=200)
cave = pyglet.sprite.Sprite(cavesmal,x=100, y=200)
 


keys = pyglet.window.key.KeyStateHandler()


def update (dt):
    global life
    life == 10
    min_x = -spr.image.width / 2

    max_x = 700 + spr.image.width / 2
    
   
    print(life)
    window.push_handlers(keys)
    if keys[pyglet.window.key.RIGHT]:
        spr.x +=1

    if keys[pyglet.window.key.LEFT]:
        spr.x -=1
    if spr.x <=0:
        life= life-1
        print (life)
    if spr.x < min_x:
        spr.x = max_x
    

    

        
    

        

@window.event
def on_draw():
    window.clear()
    
    image.blit(100,150)
    cavimg.blit(200,250)
    floor.blit(300,200)
    stairs.blit(400,100)

    door.blit(500,100)
    spr.draw()
    cave.draw()
    if life <= 0:
        label.draw()
    
    

    
    
  

pyglet.clock.schedule(update)
pyglet.app.run()
