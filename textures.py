import pygame as pg
from dataclasses import dataclass
from pytmx import load_pygame


# Класс текстур и анимаций игрока
@dataclass
class PlayerTextures(object):
    IDLE_UP    = (
        pg.image.load('textures/player_sprites/idle_up_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/idle_up_2.png').convert_alpha()
    )
    RUN_UP     = (
        pg.image.load('textures/player_sprites/run_up_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/run_up_2.png').convert_alpha()
    )
    IDLE_DOWN  = (
        pg.image.load('textures/player_sprites/idle_down_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/idle_down_2.png').convert_alpha()
    )
    RUN_DOWN   = (
        pg.image.load('textures/player_sprites/run_down_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/run_down_2.png').convert_alpha()
    )
    IDLE_LEFT  = (
        pg.image.load('textures/player_sprites/idle_left_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/idle_left_2.png').convert_alpha()
    )
    RUN_LEFT   = (
        pg.image.load('textures/player_sprites/run_left_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/run_left_2.png').convert_alpha()
    )
    IDLE_RIGHT = (
        pg.image.load('textures/player_sprites/idle_right_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/idle_right_2.png').convert_alpha()
    )
    RUN_RIGHT  = (
        pg.image.load('textures/player_sprites/run_right_1.png').convert_alpha(),
        pg.image.load('textures/player_sprites/run_right_2.png').convert_alpha()
    )

# Класс текстур мира
@dataclass
class Map(object):
    tmx_data = load_pygame('scenes/SCENE1.tmx')