import random
import json
import os

from pico2d import *
import game_framework
import start_state
import PlayerStat
from EndBg import EndBg
import Object_mgr

def enter():
    global Bg_Image, TextBox, font, agree, music
    Bg_Image = load_image('Resorce\EDN_bg.png')
    font = load_font('neodgm.TTF', 120)
    music = EndBg()
    Object_mgr.add_object(music, 5)
def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             game_framework.quit()

def update():
    for game_object in Object_mgr.all_objects():
        game_object.update()

def draw():
    global Bg_Image
    clear_canvas()
    Bg_Image.draw(640, 512)
    font.draw(350, 800, 'W I N', (0, 0, 0))
    font1 = load_font('neodgm.TTF', 60)
    font1.draw(350, 600, 'Your Grade Is', (0, 0, 0))
    font2 = load_font('neodgm.TTF', 150)
    if PlayerStat.hitCnt >= 7:
        font2.draw(850, 600, 'D', (255, 0, 0))
    elif PlayerStat.hitCnt >= 6:
        font2.draw(850, 600, 'D+', (255, 0, 0))
    elif PlayerStat.hitCnt >= 5:
        font2.draw(850, 600, 'C', (255, 0, 0))
    elif PlayerStat.hitCnt >= 4:
        font2.draw(850, 600, 'C+', (255, 0, 0))
    elif PlayerStat.hitCnt >= 3:
        font2.draw(850, 600, 'B', (255, 0, 0))
    elif PlayerStat.hitCnt >= 2:
        font2.draw(850, 600, 'B+', (255, 0, 0))
    elif PlayerStat.hitCnt >= 1:
        font2.draw(850, 600, 'A', (255, 0, 0))
    elif PlayerStat.hitCnt == 0:
        font2.draw(850, 600, 'A+', (255, 0, 0))
    update_canvas()