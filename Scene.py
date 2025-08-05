import pygame as pg
from config import Config, Color
from textures import Map

cfg = Config()
color = Color()
my_map = Map()

# Класс Сцены
class Scene(object):
    def __init__(self) -> None:
        self.model = pg.Surface((cfg.W, cfg.H))
        self.W = cfg.W
        self.H = cfg.H
        self.x, self.y = 0, 0
    
    def draw(self) -> None:
        for layer in my_map.tmx_data.visible_layers:
            for x, y, gid in layer:
                if gid:
                    tile = my_map.tmx_data.get_tile_image_by_gid(gid)
                    cfg.screen.blit(tile, (x * my_map.tmx_data.tilewidth, y * my_map.tmx_data.tileheight))