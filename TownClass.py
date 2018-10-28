from pico2d import *
import Object_mgr
import PlayerClass

class Townmap:
    image = None

    def __init__(self, x = 1920, y = 512):
        if Townmap.image == None:
            Townmap.image = load_image('Resorce\Town_map.png')
        self.x, self.y

    def deaw(self):
        self.image.draw(self.x, self.y)

    def update(self):
