import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


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


def check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    '''点击play按钮开始游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌
        sb.prep_score()
        sb.prep_level()
        sb.prep_high_score()
        sb.prep_ship()

        # 清空外形列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时重回屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重回所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    # 显示外星人
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 游戏处于非激活状态，显示按钮
    if not stats.game_active:
        play_button.draw_button()

        # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''更新子弹位置，并删除消失的子弹'''
    # 更新子弹位置
    bullets.update()  # 编组Group的upddate方法

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中外星人
    # 如果是这样就删除相应的子弹和外星人
    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''相应子弹和外星人的碰撞'''
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if not aliens:
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_alien_x(ai_settins, alien_width):
    '''计算每行可容纳多少个外星人'''
    available_sapce_x = ai_settins.screen_width - 2 * alien_width
    number_alien_x = int(available_sapce_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''' 创建一个外星人并将其放入当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    availabel_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(availabel_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人，并计算一行能容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # available_sapce_x = ai_settings.screen_width - 2 * alien_width
    # number_alien_x = int(available_sapce_x / (2 * alien_width))
    number_alien_x = get_number_alien_x(ai_settings, alien_width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # 创建一个外星人并将其加入当前行
            # alien = Alien(ai_settings, screen)
            # alien.x = alien_width + (2 * alien_width * alien_number)
            # alien.rect.x = alien.x
            # aliens.add(alien)
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''响应别外星人撞到的飞船'''
    # 将ship_left 减 1
    if stats.ships_left > 1:
        stats.ships_left -= 1

        sb.prep_ship()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''检查是否有外星人到达屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''更新外星人群众所有外星人的位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  # 对编组中所有外星人调用update方法

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    '''有外星人到达屏幕边缘时采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
