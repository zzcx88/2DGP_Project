import game_framework
import town_state
import boss_field_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image, font
    image = load_image('Resorce\Title_bg.png')
    font = load_font('neodgm.TTF', 80)

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(town_state)



def draw():
    global font
    clear_canvas()
    image.draw(640, 512)
    font.draw(550, 450, 'PRESS SPACE KEY', (0, 0, 0))
    update_canvas()




def update():
    pass


def pause():
    pass


def resume():
    pass