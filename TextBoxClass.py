from pico2d import *
import Object_mgr
import town_state
import PlayerStat
import game_framework

def Boss1_text():
    TextBox = load_image('Resorce\TextBox_1.png')
    TextBox.draw(640, 200)
    font = load_font('neodgm.TTF', 30)
    font.draw(270, 260, 'SCRIPT LEE:', (255, 0, 0))
    font = load_font('neodgm.TTF', 25)
    font.draw(260, 190, '.....나는 스크립트언어와 인공지능을 담당하는 SCRIPT LEE', (255, 255, 255))
    font.draw(260, 160, '자네의 API활용 능력을 확인해보도록 하겠네 (계속 하려면 ESC)', (255, 255, 255))

def Boss_text1():
    TextBox = load_image('Resorce\TextBox_1.png')
    TextBox.draw(640, 200)
    font = load_font('neodgm.TTF', 30)
    font.draw(270, 260, 'SCRIPT LEE:', (255, 0, 0))
    font = load_font('neodgm.TTF', 25)
    font.draw(300, 220, '.....훌륭하군', (255, 255, 255))
    font.draw(300, 190, '수업시간엔 대답좀 해주게나', (255, 255, 0))
    font.draw(300, 160, '(계속하려면 ESC)', (255, 255, 255))

def Boss_text2():
    TextBox = load_image('Resorce\TextBox_1.png')
    TextBox.draw(640, 200)
    font = load_font('neodgm.TTF', 30)
    font.draw(270, 260, 'DATA JANG:', (255, 0, 0))
    font = load_font('neodgm.TTF', 25)
    font.draw(260, 190, '자네는 링크드 리스트를 좋아하는가?', (255, 255, 255))
    font.draw(260, 160, '메모리와의 싸움에서 스스로를 증명해보아라... (계속 하려면 ESC)', (255, 255, 255))

def Boss_text3():
    TextBox = load_image('Resorce\TextBox_1.png')
    TextBox.draw(640, 200)
    font = load_font('neodgm.TTF', 30)
    font.draw(270, 260, 'DATA JANG:', (255, 0, 0))
    font = load_font('neodgm.TTF', 25)
    font.draw(300, 220, '.....용캐 해냈군', (255, 255, 255))
    font.draw(300, 190, '데이터베이스 수업때 다시 만나지....', (255, 255, 0))
    font.draw(300, 160, '(계속하려면 ESC)', (255, 255, 255))

class TextBox:
    def __init__(self):
        self.txtCnt = PlayerStat.textCnt

    def draw(self):
        if self.txtCnt == 0:
            Boss1_text()
        elif self.txtCnt == 1:
            Boss_text1()
        elif self.txtCnt == 2:
            Boss_text2()
        elif self.txtCnt == 3:
            Boss_text3()

    def update(self):
        pass