from pico2d import *
import game_framework
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 10          # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12

class FirstPatern:
    @staticmethod
    def enter(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.velocity += RUN_SPEED_PPS
        elif scriptLEE.dir == -1:
            scriptLEE.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(scriptLEE):
        if scriptLEE.hp <= 500:
            scriptLEE.cur_state = SecondPatern

    @staticmethod
    def do(scriptLEE):
        scriptLEE.frame = (scriptLEE.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        scriptLEE.x += scriptLEE.velocity * game_framework.frame_time
        if scriptLEE.x <= 80:
            scriptLEE.dir = 1
        elif scriptLEE.x >= 1200:
            scriptLEE.dir = -1

    @staticmethod
    def draw(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 256, 128, 256, scriptLEE.x, scriptLEE.y)
        else:
            scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 0, 128, 256, scriptLEE.x, scriptLEE.y)


class SecondPatern:
    @staticmethod
    def enter(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.velocity += (RUN_SPEED_PPS + 5)
        elif scriptLEE.dir == -1:
            scriptLEE.velocity -= (RUN_SPEED_PPS + 5)

    @staticmethod
    def exit(scriptLEE):
        if scriptLEE.hp <= 0:
            pass

    @staticmethod
    def do(scriptLEE):
        if scriptLEE.y == 200:
            if scriptLEE.y >= 800:
                pass
            else:
                scriptLEE.y += scriptLEE.velocity * game_framework.frame_time

        scriptLEE.frame = (scriptLEE.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        scriptLEE.x += scriptLEE.velocity * game_framework.frame_time
        if scriptLEE.x <= 80:
            scriptLEE.dir = 1

        elif scriptLEE.x >= 1200:
            scriptLEE.dir = -1

    @staticmethod
    def draw(scriptLEE):
        if scriptLEE.dir == 1:
            scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 256, 128, 256, scriptLEE.x, scriptLEE.y)
        else:
            scriptLEE.image.clip_draw(int(scriptLEE.frame) * 128, 0, 128, 256, scriptLEE.x, scriptLEE.y)


class AttackState:
    pass

class scriptLEE:
    def __init__(self):
        self.image = load_image('Resorce\LeeJY.png')
        self.x = 800
        self.y = 200
        self.hp = 1000
        self.velocity = 0
        self.dir = 1
        self.frame = 0
        self.shootPoint = 0
        #self.mapinfo = Object_mgr.find_curtain_object(0,0)
        self.cur_state = FirstPatern
        self.cur_state.enter(self)
    def draw(self):
        self.cur_state.draw(self)
    def update(self):
        #print(self.cur_state)
        self.x = clamp(80, self.x, 1280 - 80)
        self.y = clamp(110, self.y, 1024 + 128)
        self.cur_state.do(self)
        self.cur_state.exit(self)
        self.cur_state.enter(self)