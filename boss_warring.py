import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import town_state
import title_state
import boss_field_state
name = "BossWarring"


def enter():
    global TextBox, font
    TextBox = load_image('Resorce\TextBox_1.png')
    font = load_font('neodgm.TTF', 25)

def exit():
    global TextBox,font
    del (TextBox)
    del (font)


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
             game_framework.pop_state()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
             title_state.bgm.set_volume(0)
             game_framework.change_state(boss_field_state)
    #pass

def update():
    pass

def draw():
    global TextBox, font
    clear_canvas()
    town_state.TownMap.draw()
    town_state.player.draw()
    TextBox.draw(640, 200)
    font.draw(300, 220, '이곳은 공학관E동입니다.', (255, 255, 255))
    font.draw(300, 190, '정말로 이 지옥에 들어갈 준비가 되었습니까?', (255, 255, 0))
    font.draw(300, 160, '(입장 : 스페이스, 나가기 : ESC)', (255, 255, 255))
    update_canvas()