from pico2d import *
import Object_mgr
import math
import game_framework
import boss_field_state
PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
SHOOT_SPEED_KMPH = 60.0          # humuns average run speed(Km / Hour)
SHOOT_SPEED_MPM = (SHOOT_SPEED_KMPH * 1000.0 / 60.0)
SHOOT_SPEED_MPS = (SHOOT_SPEED_MPM / 60.0)
SHOOT_SPEED_PPS = (SHOOT_SPEED_MPS * PIXEL_PER_METER)

class BossBullet:
    image = None
    def __init__(self, x = 400, y = 300):
        if BossBullet.image == None:
            BossBullet.image = load_image('Resorce\EnemysBullet.png')
        self.x, self.y, self.velocity = x, y, SHOOT_SPEED_PPS

    def draw(self):
        self.image.clip_draw(0, 822, 384, 64, self.x, self.y, 350, 150)

    def get_bb(self):
        return self.x - 160, self.y - 50, self.x + 160, self.y + 50

    def update(self):
        self.y -= self.velocity * game_framework.frame_time

        if self.x < -100 or self.x > 1300 or self.y <= -10:
            Object_mgr.remove_object(self)

class BossNode:
    image = None
    def __init__(self,x,y):
        if BossNode.image == None:
            BossNode.image = load_image('Resorce\EnemysBullet.png')
        self.x, self.y, self.velocity = x, y, SHOOT_SPEED_PPS

    def draw(self):
        self.image.clip_composite_draw(0, 886, 256, 64, math.radians(90), ' ',self.x, self.y, 256, 64)

    def get_bb(self):
        return self.x - 32, self.y - 128, self.x + 25, self.y + 128

    def update(self):
        self.y -= self.velocity * game_framework.frame_time *2

        if self.x < -100 or self.x > 1300 or self.y <= -10:
            Object_mgr.remove_object(self)

class BossRuntime:
    image = None

    def __init__(self, x, y):
        if BossRuntime.image == None:
            BossRuntime.image = load_image('Resorce\EnemysBullet.png')
        self.x, self.y, self.velocity = x, y, SHOOT_SPEED_PPS

    def draw(self):
        self.image.clip_draw(448, 950, 320, 64, self.x, self.y, 600, 200)

    def get_bb(self):
        return self.x - 250, self.y - 80, self.x + 250, self.y + 80

    def update(self):
        self.x += self.velocity * game_framework.frame_time * 2

        if self.x < -100 or self.x > 1300 or self.y <= -10:
            Object_mgr.remove_object(self)

class BossOmok:
    image = None
    def __init__(self, x, y ,px, py, shootPoint):
        if BossOmok.image == None:
            BossOmok.image = load_image('Resorce\EnemysBullet.png')
        self.x, self.y, self.velocity = x, y, SHOOT_SPEED_PPS
        self.px = px
        self.py = py
        self.color = shootPoint
        self.px = clamp(80, self.px, 1280 - 80)
    def draw(self):
        if self.color % 2 == 0:
            self.image.clip_draw(768, 950, 64, 74, self.x, self.y, 80, 80)
        else:
            self.image.clip_draw(832, 950, 64, 74, self.x, self.y, 80, 80)

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 40, self.y + 40

    def update(self):
        self.x = (1 - (self.velocity * game_framework.frame_time * 2) / 250) * self.x + (self.velocity * game_framework.frame_time * 2) / 250 * self.px
        self.y -= (self.velocity * game_framework.frame_time * 2)

        if self.x < -100 or self.x > 1300 or self.y <= 130:
            Object_mgr.remove_object(self)