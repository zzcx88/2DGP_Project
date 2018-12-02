import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import town_state
import PlayerStat
name = "ShopStateTIP"

def enter():
    global Bg_Image, TextBox, font, agree, statUP_sound, worng_sound
    Bg_Image = load_image('Resorce\TIP.png')
    TextBox = load_image('Resorce\TextBox_1.png')
    font = load_font('neodgm.TTF', 25)
    agree = False
    statUP_sound = load_wav('Resorce\sound\level_up.wav')
    statUP_sound.set_volume(32)

    worng_sound = load_wav('Resorce\sound\wrong.wav')
    worng_sound.set_volume(32)

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
     global agree, statUP_sound, worng_sound
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
                 worng_sound.play()
                 draw()
             else:
                 PlayerStat.Act_Cnt -= 1
                 agree = True
                 if PlayerStat.Act_Cnt < 0:
                     pass
                 else:
                     statUP_sound.play()
                     PlayerStat.MAX_HP_Point += 1
                     PlayerStat.HP_Point = PlayerStat.MAX_HP_Point

    #pass

def update():
    pass

def draw():
    global Bg_Image, TextBox, font, agree
    if PlayerStat.Act_Cnt == -1:
        clear_canvas()
        Bg_Image.draw(640, 512)
        TextBox.draw(640, 200)
        font.draw(300, 220, '행동력이 부족합니다', (255, 255, 0))
        update_canvas()
    elif agree == True:
        clear_canvas()
        Bg_Image.draw(640, 512)
        TextBox.draw(640, 200)
        font.draw(300, 220, '체력 상승', (255, 255, 0))
        update_canvas()
    else:
         clear_canvas()
         Bg_Image.draw(640, 512)
         TextBox.draw(640, 200)
         font.draw(300, 220, '이곳은 TIP(기술혁신파크) 입니다.', (255,255,255))
         font.draw(300,190,'학식을 통해 체력 최대치를 증가시킬수 있습니다. (행동력 -1)',(255,255,255))
         font.draw(300, 160, '(나가기 ESC, 학식먹기: Y)', (255, 255, 0))
         update_canvas()