from pico2d import *
import game_framework
from BossBullet import BossNode
from BossBullet import BossRuntime
from BossBullet import BossOmok
import random
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

alphaSwitch = True
attCnt = 0
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

def random_node_attack(DataJang):
    global alphaSwitch, attCnt
    if attCnt == 5:
        pass
    elif attCnt < 5 and attCnt != -1:
         if DataJang.frameTime >= DataJang.shootTime:
             DataJang.isShoot = True
             node = BossNode(random.randint(20, 1260), 1100)
             Object_mgr.add_object(node, 4)
             DataJang.frameTime = 0
         else:
             DataJang.frameTime += game_framework.frame_time
         if DataJang.alpha >= 1:
             alphaSwitch = False
         elif DataJang.alpha <= 0:
             alphaSwitch = True
             DataJang.x = random.randint(20, 1260)
             attCnt += 1
         if alphaSwitch == True:
             DataJang.alpha += 0.015
         else:
             DataJang.alpha -= 0.015
         alpha = clamp(0, DataJang.alpha, 1)
         DataJang.image.opacify(alpha)

def horizon_attack(DataJang):
    global attCnt
    if attCnt == 5:
        if DataJang.frameTime >= DataJang.shootTime + 1:
            DataJang.isShoot = True
            Runtime = BossRuntime(0, 200)
            Object_mgr.add_object(Runtime, 4)
            DataJang.frameTime = 0
            attCnt = -1
        else:
            DataJang.frameTime += game_framework.frame_time
    else:
        if DataJang.frameTime >= DataJang.shootTime + 1:
            attCnt = 0
            DataJang.shootPoint += 1
        else:
            DataJang.frameTime += game_framework.frame_time

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
        if DataJang.hp <= 0:
            DataJang.isDead = True
        if DataJang.shootPoint == 2:
           DataJang.dir = -1
           DataJang.image.opacify(1)
           DataJang.cur_state = SecondPatern
           pass

    @staticmethod
    def do(DataJang):
        if DataJang.y <= 800:
            DataJang.alpha += 0.015
            DataJang.image.opacify(DataJang.alpha)
            DataJang.y += DataJang.velocity * game_framework.frame_time / 5
        else:
            DataJang.velocity = 0
            random_node_attack(DataJang)
            horizon_attack(DataJang)

    @staticmethod
    def draw(DataJang):
        draw_logic(DataJang)


class SecondPatern:
    @staticmethod
    def enter(DataJang):
        if DataJang.dir == -1:
            DataJang.velocity -= RUN_SPEED_PPS / 3

    @staticmethod
    def exit(DataJang):
         if DataJang.hp <= 0:
             DataJang.isDead = True

    @staticmethod
    def do(DataJang):
        if DataJang.x > 20:
            velocity_aplicate(DataJang)
        else:
            pass
        shootTime = 0.09
        if DataJang.shootPoint == 40:
            if DataJang.frameTime >= DataJang.shootTime * 3:
                DataJang.shootPoint = 0
                DataJang.cur_state = FirstPatern
            else:
                DataJang.frameTime += game_framework.frame_time
        else:
            if DataJang.frameTime >= shootTime:
                DataJang.isShoot = True
                DataJang.shootPoint += 1
                Object_mgr.add_object(BossOmok(DataJang.x, DataJang.y,
                    Object_mgr.find_curtain_object(2,0).x, Object_mgr.find_curtain_object(2,0).y,DataJang.shootPoint), 4)
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
        self.alpha = 0
        self.shootPoint = 0
        self.frameTime = 0
        self.moveTime = 1.5
        self.moveFrameTime = 0
        self.isMove = False
        self.isCollide = False
        self.isShoot = False
        self.isDead = False
        self.shootTime = 0.3
        #self.mapinfo = Object_mgr.find_curtain_object(0,0)
        self.cur_state = FirstPatern
        self.cur_state.enter(self)

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - 50, self.y - 130, self.x + 50, self.y + 110

    def update(self):
        #print(self.hp)
        self.x = clamp(80, self.x, 1280 - 80)
        self.y = clamp(110, self.y, 1024 + 128)
        self.cur_state.do(self)
        self.cur_state.exit(self)
        self.cur_state.enter(self)