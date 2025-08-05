from config import Config, Color
from Player import Player
from Scene import Scene

import pygame as pg
import colorama

pg.init()


def main() -> None:
    cfg    = Config()
    color  = Color()
    scene  = Scene()
    player = Player()
    
    gameRun = True
    # Основной цикл игры
    while gameRun:
        # Обработка событий
        for event in pg.event.get():
            # Выход
            if event.type == pg.QUIT:
                gameRun = False


        # Управление персонажем клавиатура
        keys = pg.key.get_pressed()
        key_mapping = {
            'left': (pg.K_LEFT, pg.K_a),
            'right': (pg.K_RIGHT, pg.K_d),
            'up': (pg.K_UP, pg.K_w),
            'down': (pg.K_DOWN, pg.K_s)
        }
        for direction, keys_mapping in key_mapping.items():
            if keys[keys_mapping[0]] or keys[keys_mapping[1]]:
                player.move(direction)
                

        # Обновление экрана
        cfg.screen.fill(color.WHITE)
        scene.draw()
        player.draw()
        cfg.clock.tick(cfg.FPS)
        pg.display.update()

        
    pg.quit()
    print(f'{colorama.Fore.YELLOW}Код 0{colorama.Fore.WHITE}')


if __name__ == '__main__':
    main()