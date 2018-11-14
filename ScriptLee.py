from pico2d import *
import game_framework
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 30.0          # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12

#Player Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, CTRL = range(6)

key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL
}

#Player Status

class IdleState:
    pass

class RunState:
    pass

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState}
}

class AttackState:
    pass

class scriptLEE:
    def __init__(self):
        self.x = 800
        self.y = 110
    def draw(self):
        pass
    def update(self):
        pass