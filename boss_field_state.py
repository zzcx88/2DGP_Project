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
from ScriptLee import scriptLEE
import PlayerStat
import PlayerStat
from playerBullet import PlayerBullet
name = "BossFieldState"
player = None
E_dongMap = None
txtbox = None
script_lee = None
battleStart = False
bulletList = []
shooCnt = 0
def enter():
    global battleStart
    if battleStart == False:
        global txtbox, E_dongMap, BossType, player, boss
        Object_mgr.clear_and_create_new_Objects()
        BossType = 0
        player = Player()
        E_dongMap = E_dong()
        txtbox = TextBox()
        if PlayerStat.bossType == 0:
            boss = scriptLEE()
        else:
            pass
        Object_mgr.add_object(player, 2)
        Object_mgr.add_object(E_dongMap, 0)
        Object_mgr.add_object(txtbox, 1)

def exit():
    pass
    #Object_mgr.clear_and_create_new_Objects()

def pause():
    pass

def resume():
    pass

def handle_events():
     global battleStart, shooCnt
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
             if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                 keyUp = True
             else:
                 keyUp = False
             Object_mgr.add_object(PlayerBullet(player.x, player.y, player.dir,keyUp), 3)
             shooCnt += 1
         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             if battleStart == False:
                Object_mgr.remove_object(txtbox)
                Object_mgr.add_object(boss, 1)
                battleStart = True
             else:
                 game_framework.quit()
         else:
             player.handle_event(event)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def update():
    global shooCnt
    for game_object in Object_mgr.all_objects():
        game_object.update()
    if player.isCollide == True:
        if player.frameTime >= player.invincibleTime:
            player.isCollide = False
            player.frameTime = 0
        else:
            player.frameTime += game_framework.frame_time
    else:
        if collide(player, boss):
            print("COLLIDE PLAYER")
            PlayerStat.HP_Point -= 1
            player.isCollide = True
    for bullet in Object_mgr.get_layer(3):
        if collide(boss, bullet):
            Object_mgr.remove_object(bullet)
            boss.hp -= 10
            boss.isCollide = True


def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()