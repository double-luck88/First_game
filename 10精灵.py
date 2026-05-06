import pygame as pg
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load('游戏素材/img/player_left_0.png').convert_alpha()
        self.rect = image.get_rect()#rect矩形
        self.rect.center = window.get_rect().center
        self.rect.left=self.rect.left-200 #坐标向左移动200像素

    #绘制出来
    def draw(self,wnd):
        wnd.blit(self.image,self.rect)


pg.init()

window=pg.display.set_mode((800,600))

#加载图片
image=pg.image.load("游戏素材/img/player_left_0.png").convert_alpha()
rect=image.get_rect()
rect.center=window.get_rect().center

#创建一个精灵
player=Player()#构造对象
#创建精灵组
group=pg.sprite.Group()
#把精灵放在精灵组里面
group.add(player)


isRunning=True
while isRunning:
    for ev in pg.event.get():
        if ev.type==pg.QUIT:
            isRunning=False
            break

        window.fill((227,227,227))

        # window.blit(image,rect)
        #
        # player.draw(window)
        group.draw(window)
        pg.display.update()




pg.quit()

