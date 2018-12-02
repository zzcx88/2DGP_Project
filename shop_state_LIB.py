import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import town_state
import PlayerStat
name = "ShopStateLIB"


def enter():
    global Bg_Image, TextBox, font, agree
    Bg_Image = load_image('Resorce\LIB.png')
    TextBox = load_image('Resorce\TextBox_1.png')
    font = load_font('neodgm.TTF', 25)
    agree = False
def exit():
    global Bg_Image,TextBox,font
    del (Bg_Image)
    del (TextBox)
    del (font)


def pause():
    pass

def resume():
    pass

def handle_events():
     global agree
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             town_state.player.velocity = 0
             agree = False
             game_framework.pop_state()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_y:
             if PlayerStat.Act_Cnt == -1:
                 draw()
             else:
                agree = True
                PlayerStat.Act_Cnt -= 1
                if PlayerStat.Act_Cnt < 0:
                    pass
                else:
                   PlayerStat.Att_Point += 5

def update():
    pass

def draw():
    global Bg_Image, TextBox, font, agree
    if PlayerStat.Act_Cnt == -1:
        clear_canvas()
        Bg_Image.draw(640, 512)
        TextBox.draw(640, 200)
        font.draw(300, 220, '행동력이 부족합니다', (255, 225, 0))
        update_canvas()
    elif agree == True:
        clear_canvas()
        Bg_Image.draw(640, 512)
        TextBox.draw(640, 200)
        font.draw(300, 220, '공격력 상승', (255, 255, 0))
        update_canvas()
    else:
        clear_canvas()
        Bg_Image.draw(640, 512)
        TextBox.draw(640, 200)
        font.draw(300, 220, '이곳은 종합관(도서관) 입니다.', (255,255,255))
        font.draw(300,190,'공부를 하여 공격력을 올릴 수 있습니다.(행동력 -1) ',(255,255,255))
        font.draw(300, 160, '(나가기 : ESC, 공부하기 : Y)', (255, 255, 0))
        update_canvas()