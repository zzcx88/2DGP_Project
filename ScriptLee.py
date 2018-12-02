from pico2d import *
import game_framework
from TextBoxClass import TextBox
from BossBullet import BossBullet
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 10          # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12

def draw_logic(scriptLEE):
    if scriptLEE.dir == 1:
        scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 256, 128, 256, scriptLEE.x, scriptLEE.y)
    else:
        scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 0, 128, 256, scriptLEE.x, scriptLEE.y)

def velocity_aplicate(scriptLEE):
    scriptLEE.frame = (scriptLEE.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
    scriptLEE.x += scriptLEE.velocity * game_framework.frame_time
    if scriptLEE.x <= 80:
        scriptLEE.dir = 1
    elif scriptLEE.x >= 1200:
        scriptLEE.dir = -1

class FirstPatern:
    @staticmethod
    def enter(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.velocity += RUN_SPEED_PPS
        elif scriptLEE.dir == -1:
            scriptLEE.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(scriptLEE):
        global ascendX
        if scriptLEE.hp <= 500:
           scriptLEE.cur_state = SecondPatern
           pass

    @staticmethod
    def do(scriptLEE):
        velocity_aplicate(scriptLEE)

    @staticmethod
    def draw(scriptLEE):
        draw_logic(scriptLEE)


class SecondPatern:
    @staticmethod
    def enter(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.velocity += RUN_SPEED_PPS / 3
        elif scriptLEE.dir == -1:
            scriptLEE.velocity -= RUN_SPEED_PPS / 3

    @staticmethod
    def exit(scriptLEE):
        if scriptLEE.hp <= 0:
            scriptLEE.isDead = True

    @staticmethod
    def do(scriptLEE):
        global ascendX
        if scriptLEE.y <= 800:
            if scriptLEE.velocity < 0:
                scriptLEE.velocity *= -1
            else:
                scriptLEE.y += scriptLEE.velocity * game_framework.frame_time
        else:
            velocity_aplicate(scriptLEE)
            if scriptLEE.isShoot == True:
                Object_mgr.add_object(BossBullet(scriptLEE.x, scriptLEE.y), 4)
                scriptLEE.isShoot = False
            if scriptLEE.frameTime >= scriptLEE.shootTime:
                scriptLEE.isShoot = True
                scriptLEE.frameTime = 0
            else:
                scriptLEE.frameTime += game_framework.frame_time
    @staticmethod
    def draw(scriptLEE):
        draw_logic(scriptLEE)


class AttackState:
    pass

class scriptLEE:
    def __init__(self, x = 800, y = 200):
        self.image = load_image('Resorce\LeeJY.png')
        self.x = x
        self.y = y
        self.hp = 1000
        self.velocity = 0
        self.dir = 1
        self.frame = 0
        self.alpha = 1
        self.shootPoint = 0
        self.frameTime = 0
        self.isCollide = False
        self.isShoot = False
        self.isDead = False
        self.shootTime = 0.3
        self.cur_state = FirstPatern
        self.cur_state.enter(self)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 130, self.x + 50, self.y + 110

    def update(self):
        self.x = clamp(80, self.x, 1280 - 80)
        self.y = clamp(110, self.y, 1024 + 128)
        self.cur_state.do(self)
        self.cur_state.exit(self)
        self.cur_state.enter(self)