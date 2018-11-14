import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
from E_dong import E_dong
import town_state
from Player import Player
from TextBoxClass import TextBox
import PlayerStat
name = "BossFieldState"
player = None
E_dongMap = None
txtbox = None

def enter():
    print(Object_mgr.objects)
    Object_mgr.clear_and_create_new_Objects()
    global txtbox, E_dongMap, BossType, player
    BossType = 0
    player = Player()
    E_dongMap = E_dong()
    txtbox = TextBox()
    Object_mgr.add_object(player, 1)
    Object_mgr.add_object(E_dongMap, 0)
    Object_mgr.add_object(txtbox, 1)

def exit():
    Object_mgr.clear_and_create_new_Objects()

def pause():
    pass

def resume():
    pass

def handle_events():
     #global txtbox
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
              Object_mgr.remove_object(txtbox)
         else:
             player.handle_event(event)
# def battleStart():
#     global player
#     player = Player()
#     Object_mgr.add_object(player,1)

def update():
    for game_object in Object_mgr.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()