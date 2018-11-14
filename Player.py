from pico2d import *
import game_framework
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 30.0          # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
JUMP_YSPEED_PPS = 9 * (RUN_SPEED_MPS * PIXEL_PER_METER)
JUMP_XSPEED_PPS = 2 * (RUN_SPEED_MPS * PIXEL_PER_METER)
FRAME_TIME = 0.16
ACCELERATION_OF_GRAVITY = 10.0
VARIATION_OF_VELOCITY_MPS = (ACCELERATION_OF_GRAVITY * FRAME_TIME)
VARIATION_OF_VELOCITY_PPS = (VARIATION_OF_VELOCITY_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12

#Player Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, CTRL, LANDING = range(7)

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
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        if player.isJunp == True:
            pass
        else:
             if event == SPACE:
                 player.isJunp = True
                 if player.y == 110:
                          player.jump_velocity = JUMP_YSPEED_PPS
                 else:
                     player.jump_velocity = player.jump_velocity
             pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        player.x += player.velocity * game_framework.frame_time
        player.y += player.jump_velocity * game_framework.frame_time
        player.jump_velocity -= VARIATION_OF_VELOCITY_PPS
        if player.y <= 110:
            player.y = 110
            player.isJunp = False
    @staticmethod
    def draw(player):
        if player.dir == 1:
            player.image.clip_draw(0, 640, 128, 128, player.x, player.y)
        else:
            player.image.clip_draw(0, 512, 128, 128, player.x, player.y)

class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        if player.isJunp == True:
            pass
        else:
             if event == SPACE:
                 player.isJunp = True
                 if player.y == 110:
                          player.jump_velocity = JUMP_YSPEED_PPS
                 else:
                     player.jump_velocity = player.jump_velocity
             pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        player.x += player.velocity * game_framework.frame_time
        player.y += player.jump_velocity * game_framework.frame_time
        player.jump_velocity -= VARIATION_OF_VELOCITY_PPS
        if player.y <= 110:
            player.y = 110
            player.isJunp = False
        #player.x = clamp(25, player.x, 1920 - 25)
    @staticmethod
    def draw(player):
        if player.dir == 1:
            player.image.clip_draw(int(player.frame) * 128, 640, 128, 128, player.x, player.y)
        else:
            player.image.clip_draw(int(player.frame) * 128, 512, 128, 128, player.x, player.y)

# class JumpState:
#     @staticmethod
#     def enter(player, event):
#         if event == RIGHT_DOWN:
#             player.dir = 1
#             player.jump_x = JUMP_XSPEED_PPS
#         elif event == LEFT_DOWN:
#             player.dir = -1
#             player.jump_x = -JUMP_XSPEED_PPS
#         elif event == RIGHT_UP:
#             player.dir = 1
#             pass
#         elif event == LEFT_UP:
#             player.dir = -1
#             pass
#         elif event == SPACE:
#             if player.y == 110:
#                 player.velocity = JUMP_YSPEED_PPS
#             else:
#                 player.velocity = player.velocity
#         #player.dir = clamp(-1, player.velocity, 1)
#
#     @staticmethod
#     def exit(player, event):
#         pass
#
#     @staticmethod
#     def do(player):
#         player.x += player.jump_x * game_framework.frame_time
#         player.y += player.velocity * game_framework.frame_time
#         player.velocity -= VARIATION_OF_VELOCITY_PPS
#         if player.y <= 110:
#            player.y = 110
#
#     @staticmethod
#     def draw(player):
#         if player.dir == 1:
#             player.image.clip_draw(0, 640, 128, 128, player.x, player.y)
#         else:
#             player.image.clip_draw(0, 512, 128, 128, player.x, player.y)

class TransferState:
    pass

class AttackState:
    pass

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState, SPACE: IdleState}
    # JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState,
    #            RIGHT_DOWN: JumpState, SPACE: JumpState,LANDING: IdleState}
}


class Player:
    def __init__(self):
        self.image = load_image('Resorce\PlayerCharacter.png')
        self.x, self.y = 640, 0
        self.jump_x = 0
        self.velocity = 0
        self.jump_velocity = 0
        self.isJunp = False
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def Jump(self):
        self.velocity += RUN_SPEED_PPS
        self.y += self.velocity
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        print(self.cur_state)
        self.x = clamp(25, self.x, 1280 - 25)
        self.y = clamp(110, self.y, 1024 - 25)
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            self.event = self.event_que.pop()
            self.cur_state.exit(self, self.event)
            if self.isJunp == True:
                pass
            else:
                self.cur_state = next_state_table[self.cur_state][self.event]
            self.cur_state.enter(self, self.event)
    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
