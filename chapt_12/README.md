# 项目一：外星人入侵

> 在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或到达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。

1.  创建 pygame 窗口以及相应用户输入：
    * `pygame.init()`：初始化背景设置，让 pygame 能正常工作；
    * `pygame.display.set_mode((1200, 800))`：创建一个显示窗口，实参`(1200, 800)`是一个元组，指定窗口的尺寸；
    * `screen`：是一个`surface`，在 pygame 中`surface`是屏幕的一部分，用于显示游戏元素；
    * `pygame.event.get()`：访问 pygame 检测到的事件；
    * `sys.exit()`：退出游戏；
    * `pygame.display.flip()`：在每次执行的`while`循环时都绘制一个空屏幕，并擦去旧屏幕，是的新屏幕可见。（在移动游戏元素时，`pygame.display.flip()`将不断更新屏幕，已显示元素的新位置，并在原来的位置隐藏元素，从而营造出平滑移动的效果）
2.  设置背景色：
    * `screen.fill(bg_color)`：用背景色填充屏幕
3.  创建设置类：每次给游戏添加新公布时，通常也将引入一些新的设置。
4.  添加飞船图像：
    * 创建`Ship`类：负责管理飞船的大部分行为
      * `pygame.image.load(image_path)`：加载图像（pygame 默认加载位图`.bmp`），返回一个`surface`
      * `self.image.get_rect()`：获取相应`surface`的属性`rect`。处理`rect`对象时，可使用矩形四角和中心的 x 和 y 坐标。（`rect`对象的属性：`top`, `bottom`, `left`, `right`, `center`, `centerx`,`centery`, `x`和`y`（对应左上角的 x 和 y 坐标））
    * 在屏幕上绘制飞船：
5.  重构：模块`game_functions`: 存储大量让游戏运行的函数，避免`alien_invasion.py`太长，逻辑更清晰
    * `check_evnets()`：管理事件的代码
    * `update_screen(ai_settings, screen, ship)`：更新屏幕代码
6.  响应按键：每次用户按键时，都将在 pygame 中注册一个事件，事件都是通过方法`pygame.event.get()`获取的。
    * 允许不断移动：结合`KEYDOWN`和`KEYUP`以及标志位实现持续移动
7.  调整飞船速度：
8.  限制飞船的活动范围：让飞船到达屏幕边缘后停止移动
    * `self.rect.right`：返回飞船外接矩形的右边缘的 x 坐标
9.  重构`check_event()`：`KEYDOWN`和`KEYUP`事件分两个函数
10. 添加子弹设置：
    * `setting.py` 添加子弹设置
11. 创建`Bullet`类：
    * `Bullet`继承了`pygame.sprite`中的`Sprite`类。通过使用精灵，可将游戏中相关的元素编组，进而同事操作编组中的元素。
    * 子弹不是基于图形的，是使用`python.Rect()`类从空白开始创建一个矩形。
    * 编组`Group`用于存储所有的有效子弹，以便管理发射出去的所有子弹。`pygame.sprite.Group`类类似列表，但提供了有助于开发游戏的额外功能。`add()`将元素加入编组中。
    * 删除已消失的子弹：子弹抵达屏幕顶端“消失”并不是真的消失，而是因为在屏幕外无法绘制。实际上依然存在，会导致内存消耗和处理能力的问题。表示子弹的`rect`的`bottom`属性为零时，表明子弹已经穿过屏幕顶端，此时应该删除子弹
    * `for`循环中，不应该从列表或编组中删除条目，因此必须遍历编组的副本。
    * 限制子弹数:

```py
import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init() # 初始化背景设置，让pygame能正常工作
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    # 设置背景色：
    bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环是重绘屏幕
        screen.fill(bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```
