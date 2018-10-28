from pico2d import *
import Object_mgr

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

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 5

    @staticmethod
    def draw(player):
        if player.dir == 1:
            player.image.clip_draw(0, 640, 128, 128, player.x, 110)
        else:
            player.image.clip_draw(0, 512, 128, 128, player.x, 110)

class RunState:
    pass

class TransferState:
    pass

class AttackState:
    pass

class Player:
    def __init__(self):
        self.image = load_image('Resorce\PlayerCharacter.png')
        self.x, self.y = 600, 0
        self.velocity = 0
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update(self):
        pass


    def draw(self):
        if self.dir > 0:
            self.image.clip_draw(self.frame * 128, 640, 128, 128, self.x, 110)
            self.idleStatus = 0;
        elif self.dir < 0:
            self.image.clip_draw(self.frame * 128, 512, 128, 128, self.x, 110)
            self.idleStatus = 1;
        elif self.dir == 0:
            if self.idleStatus == 0:
                self.image.clip_draw(0, 640, 128, 128, self.x, 110)
            elif self.idleStatus == 1:
                self.image.clip_draw(0, 512, 128, 128, self.x, 110)
        self.frame = (self.frame + 1) % 5
        self.x += self.dir * 10
        delay(0.02)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
