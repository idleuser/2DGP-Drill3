from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

import math

def drawRect(x,y):
    while(x<760):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 10
        delay(0.01)
    while(y<550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 10
        delay(0.01)
    while(x>10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 10
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 10
        delay(0.01)

def drawCircle(x,y,r):
    angle = 450
    while(angle > 90):
        x = math.cos(angle/360*2*math.pi)*r
        y = math.sin(angle/360*2*math.pi)*r
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + x,300 + y)
        angle -= 5
        delay(0.01)

             
x = 0
y = 90
radius = 200
while(1):
    drawRect(x,y);
    drawCircle(x,y,radius);
close_canvas()
