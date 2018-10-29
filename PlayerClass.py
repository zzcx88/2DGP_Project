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
            player.velocity += 10
        elif event == LEFT_DOWN:
            player.velocity -= 10
        elif event == RIGHT_UP:
            player.velocity -= 10
        elif event == LEFT_UP:
            player.velocity += 10

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 5

    @staticmethod
    def draw(player):
        if player.dir == 10:
            player.image.clip_draw(0, 640, 128, 128, player.x, 110)
        else:
            player.image.clip_draw(0, 512, 128, 128, player.x, 110)

class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 10
        elif event == LEFT_DOWN:
            player.velocity -= 10
        elif event == RIGHT_UP:
            player.velocity -= 10
        elif event == LEFT_UP:
            player.velocity += 10
        player.dir = player.velocity

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 5
        player.x += player.velocity

    @staticmethod
    def draw(player):
        if player.velocity == 10:
            player.image.clip_draw(player.frame * 128, 640, 128, 128, player.x, 110)
        else:
            player.image.clip_draw(player.frame * 128, 512, 128, 128, player.x, 110)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState,
               RIGHT_DOWN: RunState}
}

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

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
