import Object_mgr
import game_framework
import PlayerStat
import town_state
from TextBoxClass import TextBox
from pico2d import *
from E_dong import E_dong
from playerBullet import PlayerBullet

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collideProcess(player, boss):
    if PlayerStat.HP_Point == 0:
        player.isDead = True
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
            PlayerStat.hitCnt += 1
            player.isCollide = True

        for bossBullet in Object_mgr.get_layer(4):
            if collide(player, bossBullet):
                Object_mgr.remove_object(bossBullet)
                PlayerStat.HP_Point -= 1
                PlayerStat.hitCnt += 1
                player.isCollide = True

    if boss.alpha < 0.1:
        pass
    else:
         for bullet in Object_mgr.get_layer(3):
             if collide(boss, bullet):
                 Object_mgr.remove_object(bullet)
                 boss.hp -= 200
                 boss.isCollide = True
