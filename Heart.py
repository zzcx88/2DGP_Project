from pico2d import *
import Object_mgr
import PlayerStat
import game_framework

class Heart:
    image = None
    def __init__(self):
        if Heart.image == None:
            Heart.image = load_image('Resorce\Heart.png')
        self.x = 1280 // 2
        self.y = 45

    def draw(self):
        if PlayerStat.HP_Point == 0:
            pass
        if PlayerStat.HP_Point == 1:
            self.image.clip_draw(768, 0, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 2:
            self.image.clip_draw(640, 128, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 3:
            self.image.clip_draw(512, 256, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 4:
            self.image.clip_draw(384, 384, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 5:
            self.image.clip_draw(256, 512, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 6:
            self.image.clip_draw(128, 640, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)
        if PlayerStat.HP_Point == 7:
            self.image.clip_draw(0, 768, 896, 128, self.x, self.y, 60 * PlayerStat.HP_Point, 50)

    def update(self):
        pass