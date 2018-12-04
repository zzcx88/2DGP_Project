from pico2d import *
import Object_mgr
import town_state
import game_framework
import PlayerStat
class Townmap:
    image = None

    def __init__(self):
        if Townmap.image == None:
            Townmap.image = load_image('Resorce\Town_map1.png')
        self.x = 1920
        self.y = 512
        self.bgm = 0
        if PlayerStat.bossType == 1:
            self.bgm = load_music('Resorce\sound\school_theme.mp3')
            self.bgm.set_volume(64)
            self.bgm.repeat_play()
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if (town_state.player.dir == 1 and town_state.player.velocity < 0) or (town_state.player.dir == -1 and town_state.player.velocity > 0):
            pass
        else:
            if town_state.player.dir == 1 or town_state.player.dir == -1:
                town_state.player.x -= town_state.player.velocity * game_framework.frame_time
                self.x -= town_state.player.velocity * game_framework.frame_time
            self.x = clamp(-1200, self.x, 2540)