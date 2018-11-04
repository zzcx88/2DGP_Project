from pico2d import *
import Object_mgr
import town_state
import game_framework

def Boss1_text():
    TextBox = load_image('Resorce\TextBox_1.png')
    TextBox.draw(640, 200)
    font = load_font('neodgm.TTF', 30)
    font.draw(270, 260, 'SCRIPT LEE:', (255, 0, 0))
    font = load_font('neodgm.TTF', 25)
    font.draw(300, 190, '.....알겠냐 이놈들아?', (255, 255, 255))

class TextBox:

    def __init__(self):
        self.txtCnt = 0
    def draw(self):
        if self.txtCnt == 0:
            Boss1_text()

    def update(self):
        pass