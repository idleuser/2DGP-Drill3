from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)

def run_Circle():
    print('Circle')

    import math

    r,cx,cy = 300,800//2,600//2
    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = r*math.cos(theta) + cx
        y = r*math.sin(theta) + cy
        
        draw_boy(x,y)
    
    pass

def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass
def run_right():
    print('RIGHT')
    pass
def run_bottom():
    print('BOTTOM')
    pass
def run_left():
    print('LEFT')
    pass
def run_Rect():
    print("Rect")

    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

while True:
    run_Circle()
    run_Rect()
    break

close_canvas()
