<<<<<<< Updated upstream
import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create some text
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)

# Create a sprite
ball_image = pyglet.image.load('assets/hero/Old hero.png')
ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)

# Start the event loop
=======
import pyglet
window = pyglet.window.Window()

label = pyglet.text.Label('there is something wrong with this computer',
                          font_name='Times New Roman',
                          font_size=30,
                          x=window.width//2, y=window.height//2,
                          anchor_x='5', anchor_y='6')
>>>>>>> Stashed changes
@window.event
def on_draw():
    window.clear()
    ball.x += 1
    ball.draw()

pyglet.app.run()
