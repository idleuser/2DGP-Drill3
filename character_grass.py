from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_Circle():
    print('Circle')
    pass

def run_Rect():
    print("rect")
    pass

while True:
    run_Circle()
    run_Rect()

close_canvas()
