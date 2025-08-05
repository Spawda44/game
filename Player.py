import pygame as pg
from config import Config, Color
from textures import PlayerTextures as pt

cfg = Config()
color = Color()

# Класс Игрока
class Player(object):
    SPEED: float = 0.7
    
    def __init__(self) -> None:
        self.model = pg.Surface((16, 16), pg.SRCALPHA)
        self.texture = pt.IDLE_DOWN
        self.width = 25
        self.height = 25
        self.x = cfg.W // 2 - self.width // 2
        self.y = cfg.H // 2 - self.height // 2
    
    def move(self, direction: str) -> None:
        movement = {
            'left': (-Player.SPEED, 0),
            'right': (Player.SPEED, 0),
            'up': (0, -Player.SPEED),
            'down': (0, Player.SPEED)
        }
        if direction in movement:
            dx, dy = movement[direction]
            self.x += dx
            self.y += dy

    def draw(self) -> None:
        self.model.blit(pg.transform.scale(self.texture[0], (16, 16)), (0, 0))
        cfg.screen.blit(self.model, (self.x, self.y))