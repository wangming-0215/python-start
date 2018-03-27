import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from socreboard import ScoreBoard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个窗口
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 计分
    sb = ScoreBoard(ai_settings, screen, stats)

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:
        # 监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        gf.check_events(ai_settings, screen, stats, sb, ship,
                        aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen,
                             sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()
