from pico2d import *
import Object_mgr
import game_framework
PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
SHOOT_SPEED_KMPH = 90.0          # humuns average run speed(Km / Hour)
SHOOT_SPEED_MPM = (SHOOT_SPEED_KMPH * 1000.0 / 60.0)
SHOOT_SPEED_MPS = (SHOOT_SPEED_MPM / 60.0)
SHOOT_SPEED_PPS = (SHOOT_SPEED_MPS * PIXEL_PER_METER)

class PlayerBullet:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        if PlayerBullet.image == None:
            PlayerBullet.image = load_image('Resorce\PlayerBullet.png')
        self.x, self.y, self.velocity, self.dir = x, y, SHOOT_SPEED_PPS, dir

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def update(self):
        if self.dir == 1:
            self.x += self.velocity * game_framework.frame_time
        elif self.dir == -1:
            self.x -= self.velocity * game_framework.frame_time
        elif self.dir == 2:
            self.y += self.velocity * game_framework.frame_time
        if self.x < -100 or self.x > 1300 or self.y > 1024:
            Object_mgr.remove_object(self)
