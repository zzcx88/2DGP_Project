import random
import json
import os

from pico2d import *
import game_framework
import Object_mgr
import town_state
from E_dong import E_dong
from Player import Player
from Player import AttackState
from Player import IdleState
from TextBoxClass import TextBox
from ScriptLee import scriptLEE
import PlayerStat
import PlayerStat
from playerBullet import PlayerBullet
from BossBullet import BossBullet

name = "BossFieldState"
player = None
E_dongMap = None
txtbox = None
script_lee = None
battleStart = False

def enter():
    global battleStart
    if battleStart == False:
        global txtbox, E_dongMap, player, boss
        Object_mgr.clear_and_create_new_Objects()
        player = Player(100,130)
        E_dongMap = E_dong()
        txtbox = TextBox()
        if PlayerStat.bossType == 0:
            boss = scriptLEE()
        else:
            pass
        Object_mgr.add_object(E_dongMap, 0)
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
             if event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
                 player.isUp = True
                 player.cur_state = AttackState
                 player.isAttack = True
             elif event.type == SDL_KEYDOWN and event.key == SDLK_LCTRL:
                 player.isUp = False
                 player.isAttack = True
                 player.cur_state = AttackState
             elif event.type == SDL_KEYUP and event.key == SDLK_LCTRL:
                 player.isAttack = False
                 player.cur_state = IdleState
             elif event.type == SDL_KEYUP and event.key == SDLK_LSHIFT:
                 player.isUp = False
                 player.isAttack = False
                 player.cur_state = IdleState
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
    global isUp, txtbox
    for game_object in Object_mgr.all_objects():
        game_object.update()

    if boss.isShoot == True:
        Object_mgr.add_object(BossBullet(boss.x, boss.y), 4)
        boss.isShoot = False

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

        for bossBullet in Object_mgr.get_layer(4):
            if collide(player, bossBullet):
                Object_mgr.remove_object(bossBullet)
                PlayerStat.HP_Point -= 1
                player.isCollide = True

    for bullet in Object_mgr.get_layer(3):
        if collide(boss, bullet):
            Object_mgr.remove_object(bullet)
            boss.hp -= 200
            boss.isCollide = True
    if boss.isDead == True:
        if txtbox == None:
            PlayerStat.textCnt += 1
            PlayerStat.bossType += 1
            txtbox = TextBox()
            Object_mgr.clear_and_create_new_Objects()
            Object_mgr.add_object(E_dongMap,0)
            Object_mgr.add_object(txtbox,1)
        else:
            events = get_events()
            for event in events:
                if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    Object_mgr.clear_and_create_new_Objects()
                    global battleStart
                    battleStart = False
                    game_framework.change_state(town_state)


def draw():
    #print(Object_mgr.objects)
    clear_canvas()
    for game_object in Object_mgr.all_objects():
        game_object.draw()
    update_canvas()