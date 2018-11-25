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
    Object_mgr.clear_and_create_new_Objects()
    global txtbox, E_dongMap, BossType, player, script_lee, PlayerInst
    BossType = 0
    player = Player()
    E_dongMap = E_dong()
    txtbox = TextBox()
    script_lee = scriptLEE()
    Object_mgr.add_object(player, 2)
    Object_mgr.add_object(E_dongMap, 0)
    Object_mgr.add_object(txtbox, 1)
    PlayerInst = Object_mgr.find_curtain_object(2,0)

def exit():
    Object_mgr.clear_and_create_new_Objects()

def pause():
    pass

def resume():
    pass

def handle_events():
     global battleStart, bulletList, shooCnt
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             game_framework.quit()
         elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
             # playerBullet = PlayerBullet(PlayerInst.x, PlayerInst.y, PlayerInst.dir)
             bulletList += [PlayerBullet(PlayerInst.x, PlayerInst.y, PlayerInst.dir)]
             Object_mgr.add_object(bulletList[shooCnt], 1)
             shooCnt += 1
         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             if battleStart == False:
                Object_mgr.remove_object(txtbox)
                Object_mgr.add_object(script_lee, 1)
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
    for game_object in Object_mgr.all_objects():
        game_object.update()
    if PlayerInst.isCollide == True:
        if PlayerInst.frameTime >= PlayerInst.invincibleTime:
            PlayerInst.isCollide = False
            PlayerInst.frameTime = 0
        else:
            PlayerInst.frameTime += game_framework.frame_time
    else:
        if collide(player, script_lee):
            print("COLLIDE PLAYER")
            PlayerStat.HP_Point -= 1
            PlayerInst.isCollide = True
        if bulletList == None:
            pass
        for bullet in bulletList:
            if collide(script_lee, bullet):
                script_lee.hp -= 10
                Object_mgr.remove_object(bullet)

def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()