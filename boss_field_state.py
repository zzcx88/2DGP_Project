import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import Collision_mgr
import town_state
import game_over_state
import game_win_state
from E_dong import E_dong
from Player import Player
from Player import AttackState
from Player import IdleState
from TextBoxClass import TextBox
from ScriptLee import scriptLEE
from DataJang import DataJang
from Heart import Heart
import PlayerStat

name = "BossFieldState"
player = None
E_dongMap = None
txtbox = None
script_lee = None
battleStart = False

def enter():
    PlayerStat.textCnt += 1
    global battleStart
    if battleStart == False:
        global txtbox, E_dongMap, player, boss
        Object_mgr.clear_and_create_new_Objects()
        player = Player(100,130)
        E_dongMap = E_dong()
        txtbox = TextBox()
        heart = Heart()
        if PlayerStat.bossType == 0:
            boss = scriptLEE()
        elif PlayerStat.bossType == 1:
            boss = DataJang()
        Object_mgr.add_object(E_dongMap, 0)
        Object_mgr.add_object(heart, 0)
        Object_mgr.add_object(txtbox, 1)

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
     global battleStart, txtbox
     if boss.isDead == True:
         pass
     else:
         events = get_events()
         for event in events:
             if event.type == SDL_QUIT:
                 game_framework.quit()
             if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                 player.isUp = True
                 player.shootFrameTime = 0.15
             elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
                 player.isAttack = True
                 player.shootFrameTime = 0.15
                 player.cur_state = AttackState
             elif event.type == SDL_KEYUP and event.key == SDLK_LCTRL:
                 player.isAttack = False
                 player.cur_state = IdleState
             elif event.type == SDL_KEYUP and event.key == SDLK_UP:
                 player.isUp = False
             elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                 if battleStart == False:
                    Object_mgr.remove_object(txtbox)
                    txtbox = None
                    Object_mgr.add_object(player, 2)
                    Object_mgr.add_object(boss, 1)
                    boss.x = 1000
                    boss.y = 200
                    battleStart = True
                 else:
                     game_framework.quit()
             elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
                  player.cheatEnable *= -1
             elif event.type == SDL_KEYDOWN and event.key == SDLK_F9 and player.cheatEnable == 1:
                  PlayerStat.Att_Point += 1.5
                  print('Enable_ATT_Cheat ', PlayerStat.Att_Point)
             elif event.type == SDL_KEYDOWN and event.key == SDLK_F8 and player.cheatEnable == 1:
                 PlayerStat.HP_Point = -1
                 PlayerStat.MAX_HP_Point = -1
                 print('Enable_HP_Cheat')
             elif event.type == SDL_KEYDOWN and event.key == SDLK_F7 and player.cheatEnable == 1:
                 PlayerStat.velocity += 2
                 print('Enable_velocity_Cheat ', PlayerStat.velocity)
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
    global isUp, txtbox, battleStart
    for game_object in Object_mgr.all_objects():
        game_object.update()
    Collision_mgr.collideProcess(player, boss)

    if player.isDead == True:
        Object_mgr.clear_and_create_new_Objects()
        player.isDead = False
        battleStart = False
        boss.bgm.stop()
        game_framework.change_state(game_over_state)

    if boss.isDead == True:
        if txtbox == None:
            PlayerStat.textCnt += 1
            PlayerStat.bossType += 1
            PlayerStat.Act_Cnt = 2
            PlayerStat.HP_Point = PlayerStat.MAX_HP_Point
            txtbox = TextBox()
            Object_mgr.clear_and_create_new_Objects()
            Object_mgr.add_object(E_dongMap,0)
            Object_mgr.add_object(txtbox,1)
        else:
            events = get_events()
            for event in events:
                if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    Object_mgr.clear_and_create_new_Objects()
                    battleStart = False
                    if PlayerStat.bossType == 2:
                        game_framework.change_state(game_win_state)
                    else:
                        game_framework.change_state(town_state)

def draw():
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()