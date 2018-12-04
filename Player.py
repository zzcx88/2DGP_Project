from pico2d import *
import game_framework
import PlayerStat
from playerBullet import PlayerBullet
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 30.0       # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
JUMP_YSPEED_PPS = 6 * (RUN_SPEED_MPS * PIXEL_PER_METER)
JUMP_XSPEED_PPS = 2 * (RUN_SPEED_MPS * PIXEL_PER_METER)
FRAME_TIME = 0.16
ACCELERATION_OF_GRAVITY = 13.0
VARIATION_OF_VELOCITY_MPS = (ACCELERATION_OF_GRAVITY * FRAME_TIME)
VARIATION_OF_VELOCITY_PPS = (VARIATION_OF_VELOCITY_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12

#Player Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, CTRL, CTRL_UP, L_SHIFT_UP, LANDING = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL,
    (SDL_KEYUP, SDLK_LCTRL): CTRL_UP,
    (SDL_KEYUP, SDLK_LSHIFT): L_SHIFT_UP
}

def velocity_aplicate(player):
     if player.cur_state == AttackState:
         player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
     else:
         player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
     if (player.dir == 1 and player.velocity < 0) or(player.dir == -1 and player.velocity > 0):
         pass
     else:
         player.x += player.velocity * game_framework.frame_time
         player.y += player.jump_velocity * game_framework.frame_time
         player.jump_velocity -= VARIATION_OF_VELOCITY_PPS
     if player.y <= 130:
         player.y = 130
         player.jump_velocity = 0
         player.isJunp = False
         if player.velocity == 0:
             player.cur_state = IdleState
         else:
             player.cur_state = RunState
     if player.isAttack == True:
         player.cur_state = AttackState


def jump_overlap_check(player, event):
    if player.isJunp == True:
        pass
    else:
        if event == SPACE:
            player.jump()
            player.isJunp = True
            if player.y == 130:
                player.jump_velocity = JUMP_YSPEED_PPS
            else:
                player.jump_velocity = player.jump_velocity


def velocity_acc(player, event):
    if event == RIGHT_DOWN:
        if player.CHECKR == False or player.CHECKR == True:
            player.CHECKR = True
            player.dir = 1
            player.velocity += RUN_SPEED_PPS * PlayerStat.velocity
    elif event == LEFT_DOWN:
        if player.CHECKL == False or player.CHECKL == True:
            player.CHECKL = True
            player.dir = -1
            player.velocity -= RUN_SPEED_PPS * PlayerStat.velocity
    elif event == RIGHT_UP:
        if player.CHECKR == True:
            player.velocity -= RUN_SPEED_PPS * PlayerStat.velocity
            player.CHECKR = False
    elif event == LEFT_UP:
        if player.CHECKL == True:
            player.velocity += RUN_SPEED_PPS * PlayerStat.velocity
            player.CHECKL = False

class IdleState:

    @staticmethod
    def enter(player, event):
        velocity_acc(player, event)

    @staticmethod
    def exit(player, event):
        jump_overlap_check(player, event)

    @staticmethod
    def do(player):
        velocity_aplicate(player)
    @staticmethod
    def draw(player):
        if player.dir == 1:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(0, 640, 128, 128, player.x, player.y)
            else:
                player.image.opacify(1)
                player.image.clip_draw(0, 640, 128, 128, player.x, player.y)
        else:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(0, 512, 128, 128, player.x, player.y)
            else:
                player.image.opacify(1)
                player.image.clip_draw(0, 512, 128, 128, player.x, player.y)


class RunState:
    @staticmethod
    def enter(player, event):
        velocity_acc(player, event)

    @staticmethod
    def exit(player, event):
        jump_overlap_check(player, event)

    @staticmethod
    def do(player):
        velocity_aplicate(player)

    @staticmethod
    def draw(player):
        if player.dir == 1:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(int(player.frame) * 128, 640, 128, 128, player.x, player.y, )
            else:
                player.image.opacify(1)
                player.image.clip_draw(int(player.frame) * 128, 640, 128, 128, player.x, player.y,)
        else:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(int(player.frame) * 128, 512, 128, 128, player.x, player.y)
            else:
                player.image.opacify(1)
                player.image.clip_draw(int(player.frame) * 128, 512, 128, 128, player.x, player.y)

class AttackState:
    @staticmethod
    def enter(player, event):
        velocity_acc(player, event)

    @staticmethod
    def exit(player, event):
        jump_overlap_check(player, event)

    @staticmethod
    def do(player):
        velocity_aplicate(player)

        # 플레이어 자동발사 로직
        if player.isAttack == True:
            if player.shootFrameTime >= player.shootTime:
                if player.isUp == True:
                    player.shoot()
                    Object_mgr.add_object(PlayerBullet(player.x, player.y, 2), 3)
                    player.shootFrameTime = 0
                else:
                    player.shoot()
                    Object_mgr.add_object(PlayerBullet(player.x, player.y, player.dir), 3)
                    player.shootFrameTime = 0
            else:
                player.shootFrameTime += game_framework.frame_time

    @staticmethod
    def draw(player):
        if player.dir == 1:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(int(player.frame) * 128, 384, 128, 128, player.x, player.y)
            else:
                player.image.opacify(1)
                player.image.clip_draw(int(player.frame) * 128, 384, 128, 128, player.x, player.y)
        else:
            if player.isCollide == True:
                player.image.opacify(0.5)
                player.image.clip_draw(int(player.frame) * 128, 256, 128, 128, player.x, player.y)
            else:
                player.image.opacify(1)
                player.image.clip_draw(int(player.frame) * 128, 256, 128, 128, player.x, player.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE: IdleState, CTRL: AttackState, CTRL_UP: IdleState, L_SHIFT_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState, SPACE: IdleState,CTRL: AttackState,CTRL_UP: IdleState, L_SHIFT_UP: IdleState},
     AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: AttackState,
                RIGHT_DOWN: AttackState, SPACE: AttackState,CTRL: AttackState,CTRL_UP: IdleState, L_SHIFT_UP: IdleState}
}


class Player:
    def __init__(self,x = 640, y = 0):
        self.image = load_image('Resorce\PlayerCharacter.png')
        self.x, self.y = x, y
        self.jump_x = 0
        self.velocity = 0
        self.jump_velocity = 0
        self.CHECKR = False
        self.CHECKL = False
        self.isDead = False
        self.isJunp = False
        self.isCollide = False
        self.isAttack = False
        self.isUp = False
        self.shootTime = 0.1
        self.shootFrameTime = 0
        self.invincibleTime = 2
        self.frameTime = 0
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.shoot_sound = load_wav('Resorce\sound\shoot.wav')
        self.shoot_sound.set_volume(32)

        self.hurt_sound = load_wav('Resorce\sound\hurt.wav')
        self.hurt_sound.set_volume(32)

        self.jump_sound = load_wav('Resorce\sound\jump.wav')
        self.jump_sound.set_volume(32)

        self.cheatEnable = -1



    def get_bb(self):
        return self.x - 30, self.y - 59, self.x + 30, self.y + 40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.x = clamp(25, self.x, 1280 - 25)
        self.y = clamp(110, self.y, 1024 - 25)
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            self.event = self.event_que.pop()
            self.cur_state.exit(self, self.event)
            self.cur_state = next_state_table[self.cur_state][self.event]
            self.cur_state.enter(self, self.event)

    def draw(self):
        self.cur_state.draw(self)

    def shoot(self):
        self.shoot_sound.play()

    def hurt(self):
        self.hurt_sound.play()

    def jump(self):
        self.jump_sound.play()

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
