from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

player = FirstPersonController(position = (0,20,0))
Sky()
spawn = Entity(model = "cube", scale = (4,0.5,4), color = color.red, collider = "mesh",Texture="white_cube", position = (0,0,0))
x,y,z=6.5,0,0
for i in range(random.randint(10,50)):

    y= random.uniform(-1,1)
    z=random.uniform(-3,3)
    block = Entity(model = "cube", scale = (4,0.5,4), color = color.green, collider = "mesh",Texture="white_cube", position = (x,y,z))
    x+= 6

finish = Entity(model = "cube", scale = (4,0.5,4), color = color.blue, collider = "mesh",Texture="white_cube", position = (x,0,0))

def update():
    if player.y < -10:
        player.position = (0,20,0)
    if player.x== x:
        text = Text(text="You won!!",positon = (x,20))
        player.position = (0,20,0)
app.run()