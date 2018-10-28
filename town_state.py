import random
import json
import os

from pico2d import *
import game_framework
import PlayerClass


name = "TownState"


def enter():
    global player
    player = PlayerClass.Player()
    global TownBg
    TownBg = load_image('Resorce\Town_map.png')
    global x, y
    x = 1920
    y = 512


def exit():
    global TownBg
    del (TownBg)


def pause():
    pass

def resume():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.dir += 1
            elif event.key == SDLK_LEFT:
                player.dir -= 1
            elif event.key == SDLK_ESCAPE:
                player.running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1

def update():
    global x
    global player
    if player.x > 1300 // 2:
        player.x -= 10
        x -= 10
    elif player.x < 600:
        player.x += 10
        x += 10

def draw():
    global player
    clear_canvas()
    TownBg.draw(x, y)
    player.update()
    player.draw()
    update_canvas()





