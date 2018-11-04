from pico2d import *
import Object_mgr
import town_state
import game_framework

class E_dong:
    image = None
    def __init__(self):
        if E_dong.image == None:
            E_dong.image = load_image('Resorce\LectureRoom.png')
        self.x = 640
        self.y = 512
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass