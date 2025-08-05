from dataclasses import dataclass
import colorama
import pygame as pg
from materials import Music

music = Music()

# Класс для определения цвета в будущем расширяемый
@dataclass
class Color(object):
    WHITE = (255, 255, 255) 
    BLACK = (0, 0, 0)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)
    ALL   = (WHITE, BLACK, RED, GREEN, BLUE)
    
    GRASS = (141, 156, 51)
    

# Класс для конфигурации игры и окна
@dataclass
class Config(object):
    IS_RESIZIBLE = False
    
    W, H   = 480, 480
    screen = pg.display.set_mode((W, H), pg.RESIZABLE if IS_RESIZIBLE else 0)
    name   = pg.display.set_caption('Something...')
    clock  = pg.time.Clock()
    mixer  = pg.mixer.init()
    FPS    = 120
    
    try:
        icon = pg.display.set_icon(pg.image.load('textures/viviavi.jpg'))
    except FileNotFoundError:
        print(f'{colorama.Fore.RED}Ошибка! Иконка не найдена...{colorama.Fore.WHITE}')
    print(f'{colorama.Fore.GREEN}Успех!{colorama.Fore.WHITE}')
        
    pg.mixer.music.load(music.MAIN_THEME)
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.2)