import pygame as pg
from pygame.sprite import Sprite
from typing import List,Tuple


class Animation(Sprite):
    def __init__(self,pos:Tuple[int,int] ,filenames:List[str]):#tuple元组
        super().__init__()
        self.images:list[pg.Surface]=[]
        for filename in filenames:
            self.images.append(pg.image.load(filename))
        self.index=0
        self.counter=0
        self.delay=100


        self.image=self.images[self.index]
        self.rect=pg.rect.Rect(pos[0],pos[1],self.image.get_width(),self.image.get_height())


    def update(self,*args,**kwargs):
        self.counter += 1
        # #1，通过帧率控制动画速度
        # if self.counter>self.delay:
        #     self.index+=1
        #     if self.index==len(self.images):
        #         self.index=0
        #     self.counter=0
        #通过时间控制速度
        self.index=int((pg.time.get_ticks()/self.delay)%len(self.images))

        self.image=self.images[self.index]
        print(f"index is {self.index}")

pg.init()

window=pg.display.set_mode((800,600))

clock=pg.time.Clock()

frame_list=[
    '游戏素材/img/player_left_0.png',
    '游戏素材/img/player_left_1.png',
    '游戏素材/img/player_left_2.png',
    '游戏素材/img/player_left_3.png',
    '游戏素材/img/player_left_4.png',
    '游戏素材/img/player_left_5.png',
]

#创建一个动画
anima=Animation((20,20),frame_list)
#创建精灵组
group=pg.sprite.Group()
#把精灵添加到精灵组中
group.add(anima)




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

        group.update()
        pg.display.update()
        clock.tick(60)#控制帧率



pg.quit()

