from pico2d import *
import Object_mgr
import town_state
import game_framework
class Townmap:
    image = None

    def __init__(self):
        if Townmap.image == None:
            Townmap.image = load_image('Resorce\Town_map1.png')
        self.x = 1920
        self.y = 512
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        #print(self.x)
        if town_state.player.x > 1280 // 2:
            town_state.player.x -= town_state.player.velocity * game_framework.frame_time
            self.x -= town_state.player.velocity * game_framework.frame_time
        self.x = clamp(-1200, self.x, 2540)