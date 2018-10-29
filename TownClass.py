from pico2d import *
import Object_mgr
import town_state

class Townmap:
    image = None

    def __init__(self):
        if Townmap.image == None:
            Townmap.image = load_image('Resorce\Town_map.png')
        self.x = 1920
        self.y = 512

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if town_state.player.x > 1300 // 2:
           town_state.player.x -= 10
           self.x -= 10
        elif town_state.player.x < 600:
             town_state.player.x += 10
             self.x += 10
