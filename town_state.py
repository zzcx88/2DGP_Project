import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import shop_state_TIP
import shop_state_GYM
import shop_state_LIB
import title_state
import PlayerStat
import boss_warring
from Player import Player
from Heart import Heart
from Town import Townmap
from Player import *
name = "TownState"

player = None
TownMap = None


TIP, GYM, LIB, G_DONG, E_DONG = range(5)

Shop_point_table = {
    TIP:range(2540, 1690,-1),
    GYM:range(1550,1330,-1) ,
    LIB:range(1100, 530,-1),
    G_DONG:range(170, -350,-1),
    E_DONG:range(-600, -1200,-1),
}

def enter():
    global player, TownMap, x, dir
    player = Player()
    TownMap = Townmap()
    heart = Heart()
    Object_mgr.add_object(heart, 2)
    Object_mgr.add_object(TownMap, 0)
    Object_mgr.add_object(player, 1)
    if PlayerStat.bossType == 1:
        TownMap.image = load_image('Resorce\Town_map2.png')

def exit():
    pass

def pause():
    pass

def intoShop():
    global player, TownMap
    for x in Shop_point_table[TIP]:
        if int(TownMap.x) == x:
            Object_mgr.remove_object(player)
            game_framework.push_state(shop_state_TIP)
    for x in Shop_point_table[GYM]:
        if int(TownMap.x) == x:
            Object_mgr.remove_object(player)
            game_framework.push_state(shop_state_GYM)
    for x in Shop_point_table[LIB]:
        if int(TownMap.x) == x:
            Object_mgr.remove_object(player)
            game_framework.push_state(shop_state_LIB)
    for x in Shop_point_table[G_DONG]:
        if int(TownMap.x) == x:
            pass
    for x in Shop_point_table[E_DONG]:
        if int(TownMap.x) == x:
            Object_mgr.remove_object(player)
            game_framework.push_state(boss_warring)

def resume():
    global player, x, dir
    player = Player(x, 130)
    player.dir = dir
    Object_mgr.add_object(player, 1)

def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            intoShop()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            player.cheatEnable *= -1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F9 and player.cheatEnable == 1:
            PlayerStat.Att_Point += 1.5
            print('Enable_ATT_Cheat ' ,PlayerStat.Att_Point)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F8 and player.cheatEnable == 1:
             PlayerStat.HP_Point = -1
             PlayerStat.MAX_HP_Point = -1
             print('Enable_HP_Cheat')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F7 and player.cheatEnable == 1:
            if player.velocity == 0:
                PlayerStat.velocity += 2
                print('Enable_velocity_Cheat ', PlayerStat.velocity)
            else:
                print('Please_stop_your_character  ')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F6 and player.cheatEnable == 1:
            PlayerStat.bossType = 1
            PlayerStat.textCnt = 1
            TownMap.image = load_image('Resorce\Town_map2.png')
            title_state.bgm.set_volume(0)
            TownMap.bgm = load_music('Resorce\sound\school_theme.mp3')
            TownMap.bgm.set_volume(64)
            TownMap.bgm.repeat_play()
            print('Change_BOSS to DATA_JANG')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F5 and player.cheatEnable == 1:
            if PlayerStat.bossType == 0:
                pass
            else:
                 PlayerStat.bossType = 0
                 PlayerStat.textCnt = -1
                 TownMap.image = load_image('Resorce\Town_map1.png')
                 TownMap.bgm.stop()
                 TownMap.bgm = load_music('Resorce\sound\Title_theme.ogg')
                 TownMap.bgm.set_volume(64)
                 TownMap.bgm.repeat_play()
            print('Change_BOSS to SCRIPT_LEE')
        else:
            player.handle_event(event)

def update():
    global x, dir
    for game_object in Object_mgr.all_objects():
        game_object.update()
        x = player.x
        dir = player.dir


def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()




