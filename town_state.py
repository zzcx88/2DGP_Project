import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import shop_state_TIP
import shop_state_GYM
import shop_state_LIB
import boss_warring
from Player import Player
from Town import Townmap
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
    global player, TownMap
    player = Player()
    TownMap = Townmap()
    Object_mgr.add_object(TownMap, 0)
    Object_mgr.add_object(player, 1)

def exit():
    global player, TownMap
    Object_mgr.clear()
    del player
    del TownMap


def pause():
    pass

def intoShop():
    global player, TownMap
    for x in Shop_point_table[TIP]:
        if int(TownMap.x) == x:
            print('TIP')
            game_framework.push_state(shop_state_TIP)
    for x in Shop_point_table[GYM]:
        if int(TownMap.x) == x:
            game_framework.push_state(shop_state_GYM)
    for x in Shop_point_table[LIB]:
        if int(TownMap.x) == x:
            game_framework.push_state(shop_state_LIB)
    for x in Shop_point_table[G_DONG]:
        if int(TownMap.x) == x:
            print('G_DONG')
    for x in Shop_point_table[E_DONG]:
        if int(TownMap.x) == x:
            game_framework.push_state(boss_warring)
def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            intoShop()
        else:
            player.handle_event(event)

def update():
    for game_object in Object_mgr.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()
    #delay(0.02)





