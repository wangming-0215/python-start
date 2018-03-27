# 项目：外星人入侵

1.  对编组调用`draw()`时，pygame 会自动绘制编组中的每个元素，绘制位置由元素的属性`rect`决定
2.  `sprite.groupcollide()`：检测两个编组成员之间的碰撞
3.  `sprite.spritecollideany(sprite, group)`：检测编组是否有成员与精灵发生碰撞，并在找到与精灵发生碰撞的成员后停止遍历编组。如果没有发生碰撞，返回`None`。
4.  计分： pygame 通过将要显示的字符串渲染成图像来处理文本
5.  `collidepoint(mouse_x, mouse_y)`：检测鼠标点击的位置是否在某个`rect`内
6.  `pygame.mouse.get_pos()`：获取鼠标点击的位置
