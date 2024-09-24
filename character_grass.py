from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.05)

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
    for x in range(0,790,10):
        draw_boy(x,550)
    pass
def run_right():
    print('RIGHT')
    for y in range(550,30,-10):
        draw_boy(780,y)
    pass
def run_bottom():
    print('BOTTOM')
    for x in range(790,0,-10):
        draw_boy(x,30)
    pass
def run_left():
    print('LEFT')
    for y in range(30,550,10):
        draw_boy(10,y)
    pass
def run_Rect():
    print("Rect")

    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_left_side():
    print("left_side")
    x = 0
    for y in range(30,550,10):
        draw_boy(x,y)
        x += 7.5
    
    pass
def run_right_side():
    print("right_side")
    x = 390
    for y in range(550,30,-10):
        draw_boy(x,y)
        x += 7.5
    pass

def run_Triangle():
    print("Triangle")
    run_bottom()
    run_left_side()
    run_right_side()
    pass

while True:
    #run_Circle()
    #run_Rect()
    run_Triangle()
    break

close_canvas()
