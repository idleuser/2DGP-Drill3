from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_Circle():
    print('Circle')

    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    
    pass

def run_Rect():
    print("rect")
    pass

while True:
    run_Circle()
    run_Rect()
    break

close_canvas()
