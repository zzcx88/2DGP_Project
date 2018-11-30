from pico2d import *
import Object_mgr
import game_framework
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
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 160, self.y - 50, self.x + 160, self.y + 50

    def update(self):
        self.y -= self.velocity * game_framework.frame_time

        if self.x < -100 or self.x > 1300 or self.y <= -10:
            Object_mgr.remove_object(self)
