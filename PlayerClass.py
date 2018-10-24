from pico2d import *

class Player:
    def __init__(self):
        self.image = load_image('Resorce\PlayerCharacter.png')
        self.x, self.y = 600, 0
        self.frame = 0
        self.dir =0
        self.idleStatus = 0
        if self.image == None:
            self.image = load_image('Resorce\PlayerCharacter.png')

    def update(self):
        pass


    def draw(self):
        if self.dir > 0:
            self.image.clip_draw(self.frame * 128, 640, 128, 128, self.x, 110)
            self.idleStatus = 0;
        elif self.dir < 0:
            self.image.clip_draw(self.frame * 128, 512, 128, 128, self.x, 110)
            self.idleStatus = 1;
        elif self.dir == 0:
            if self.idleStatus == 0:
                self.image.clip_draw(0, 640, 128, 128, self.x, 110)
            elif self.idleStatus == 1:
                self.image.clip_draw(0, 512, 128, 128, self.x, 110)
        self.frame = (self.frame + 1) % 5
        self.x += self.dir * 10
        delay(0.02)
