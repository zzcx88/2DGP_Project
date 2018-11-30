from pico2d import *
import game_framework
from TextBoxClass import TextBox
import Object_mgr

PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 10          # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 12
alpha = 0
def draw_logic(DataJang):
    if DataJang.dir == 1:
        DataJang.image.clip_draw(0, 256, 128, 256, DataJang.x, DataJang.y)
    else:
        DataJang.image.clip_draw(0, 0, 128, 256, DataJang.x, DataJang.y)

def velocity_aplicate(DataJang):
    DataJang.x += DataJang.velocity * game_framework.frame_time
    if DataJang.x <= 80:
        DataJang.dir = 1
    elif DataJang.x >= 1200:
        DataJang.dir = -1

class FirstPatern:
    @staticmethod
    def enter(DataJang):
        if DataJang.dir == 1:
            DataJang.velocity += RUN_SPEED_PPS
        elif DataJang.dir == -1:
            if DataJang.y <= 800 and DataJang.cur_state == FirstPatern:
                DataJang.velocity += RUN_SPEED_PPS
            else:
                DataJang.velocity -= RUN_SPEED_PPS

    @staticmethod


    def exit(DataJang):
        if DataJang.hp <= 500:
           DataJang.cur_state = SecondPatern
           pass

    @staticmethod
    def do(DataJang):
        print(DataJang.y)
        global alpha
        if DataJang.y <= 800:
            alpha += 0.015
            DataJang.image.opacify(alpha)
            DataJang.y += DataJang.velocity * game_framework.frame_time / 5
        else:
            DataJang.image.opacify(1)


    @staticmethod
    def draw(DataJang):
        draw_logic(DataJang)


class SecondPatern:
    @staticmethod
    def enter(DataJang):
        if DataJang.dir == 1:
            DataJang.velocity += RUN_SPEED_PPS / 3
        elif DataJang.dir == -1:
            DataJang.velocity -= RUN_SPEED_PPS / 3

    @staticmethod
    def exit(DataJang):
        if DataJang.hp <= 0:
            DataJang.isDead = True

    @staticmethod
    def do(DataJang):
        if DataJang.y <= 800:
            if DataJang.velocity < 0:
                DataJang.velocity *= -1
            else:
                DataJang.y += DataJang.velocity * game_framework.frame_time
        else:
            velocity_aplicate(DataJang)

            if DataJang.frameTime >= DataJang.shootTime:
                DataJang.isShoot = True
                DataJang.frameTime = 0
            else:
                DataJang.frameTime += game_framework.frame_time
    @staticmethod
    def draw(DataJang):
        draw_logic(DataJang)


class AttackState:
    pass

class DataJang:
    def __init__(self, x = 800, y = 200):
        self.image = load_image('Resorce\Data_Jang.png')
        self.x = x
        self.y = y
        self.hp = 1000
        self.velocity = 0
        self.dir = -1
        self.shootPoint = 0
        self.frameTime = 0
        self.isCollide = False
        self.isShoot = False
        self.isDead = False
        self.shootTime = 0.3
        #self.mapinfo = Object_mgr.find_curtain_object(0,0)
        self.cur_state = FirstPatern
        self.cur_state.enter(self)
    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 50, self.y - 130, self.x + 50, self.y + 110

    def update(self):
        #print(self.hp)
        self.x = clamp(80, self.x, 1280 - 80)
        self.y = clamp(110, self.y, 1024 + 128)
        self.cur_state.do(self)
        self.cur_state.exit(self)
        self.cur_state.enter(self)