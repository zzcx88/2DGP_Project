import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
from PlayerClass import Player
from TownClass import Townmap
name = "TownState"

player = None
TownMap = None

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

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            pass
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
    delay(0.02)





