import sys
import pygame

from bullet import Bullet


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.move_right = True

    elif event.key == pygame.K_LEFT:
        ship.move_left = True

    elif event.key == pygame.K_UP:
        ship.move_up = True

    elif event.key == pygame.K_DOWN:
        ship.move_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    '''如果没有达到限制，就发射一颗子弹'''
    # 创建新子弹并将其加入到bullets编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    '''响应松开按键'''
    if event.key == pygame.K_RIGHT:
        ship.move_right = False

    elif event.key == pygame.K_LEFT:
        ship.move_left = False

    elif event.key == pygame.K_UP:
        ship.move_up = False

    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def check_events(ai_settings, screen, ship, bullets):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时重回屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重回所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    '''更新子弹位置，并删除消失的子弹'''
    # 更新子弹位置
    bullets.update()  # 编组Group的upddate方法

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
