import random
import json
import os

from pico2d import *
import game_framework
import start_state
import PlayerStat

class EndBg:
    def __init__(self):
        self.bgm = load_music('Resorce\sound\END_theme.ogg')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
    def update(self):
        pass