import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数
        # rect值存储值的整数部分
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动标志调整飞船位置'''
        # 更新飞船的center值，而不是rect
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.centerx += self.ai_settings.ship_speed_factor

        if self.move_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.centerx -= self.ai_settings.ship_speed_factor

        if self.move_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
