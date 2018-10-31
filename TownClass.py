from pico2d import *
import Object_mgr
import town_state
import game_framework
PIXEL_PER_METER = (10.0 / 0.3) # 1pixel per 3cm
RUN_SPEED_KMPH = 30.0         # humuns average run speed(Km / Hour)
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


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
           town_state.player.x -= town_state.player.velocity * game_framework.frame_time
           self.x -= town_state.player.velocity * game_framework.frame_time
        elif town_state.player.x < 600:
             town_state.player.x += town_state.player.velocity * game_framework.frame_time
             self.x += town_state.player.velocity * game_framework.frame_time
