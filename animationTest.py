from pico2d import *

open_canvas()
character = load_image('PlayerCharacter.png')


running = True
x = 0
frame = 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while x < 800 and running:
    clear_canvas()
    #grass.draw(400, 30)
    character.clip_draw(frame * 128, 630, 128, 128, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 5
    x += 5
    delay(0.05)

close_canvas()
