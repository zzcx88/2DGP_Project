import random
import json
import os

from pico2d import *
import game_framework
import start_state
import PlayerStat
def enter():
    global Bg_Image, TextBox, font, agree
    Bg_Image = load_image('Resorce\GameOver_bg.png')
    font = load_font('neodgm.TTF', 120)

def exit():
    pass

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
             PlayerStat.Att_Point = 1
             PlayerStat.HP_Point = 3
             PlayerStat.MAX_HP_Point = 3
             PlayerStat.Act_Cnt = 2
             PlayerStat.textCnt = -1
             PlayerStat.velocity = 1
             PlayerStat.bossType = 0
             PlayerStat.hitCnt = 0
             game_framework.change_state(start_state)

def update():
    pass

def draw():
    global Bg_Image
    clear_canvas()
    Bg_Image.draw(640, 512)
    font.draw(320, 800, 'GAME OVER', (255, 0, 0))
    font1 = load_font('neodgm.TTF', 60)
    font1.draw(320, 600, 'Your Grade Is', (255, 0, 0))
    font2 = load_font('neodgm.TTF', 150)
    font2.draw(850, 600, 'F', (255, 255, 0))
    update_canvas()