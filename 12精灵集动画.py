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

class AnimationSheet(Sprite):
    def __init__(self,filename,pos,scale=2):#pos坐标,scale=2是放大两倍
        super().__init__()
        self.imageSheet=pg.image.load(filename).convert_alpha()
        self.x_index=0#绘制当前的某一帧
        self.y_index=0#当前绘制哪套动画
        self.frame_size=80
        self.frame_count=6
        self.scale=scale
        self.delay=100
        self.flip=False #翻转

        self.source_rect=pg.rect.Rect(self.x_index*self.frame_size,self.y_index*self.frame_size,
                                      self.frame_size,self.frame_size)

        self.image=self.imageSheet.subsurface(self.source_rect)
        self.image=pg.transform.scale_by(self.image,self.scale)
        self.image=pg.transform.flip(self.image,self.flip,False)
        self.rect=pg.rect.Rect(pos[0],pos[1],self.frame_size*self.scale,self.frame_size*self.scale)


    def update(self,*args,**kwargs):
        self.x_index=int((pg.time.get_ticks()/self.delay)%self.frame_count)
        self.source_rect = pg.rect.Rect(self.x_index * self.frame_size, self.y_index * self.frame_size,
                                        self.frame_size, self.frame_size)

        self.image = self.imageSheet.subsurface(self.source_rect)
        self.image = pg.transform.scale_by(self.image, self.scale)
        self.image = pg.transform.flip(self.image, self.flip, False)
        print(f"x_index{self.x_index}")

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
animaSheet=AnimationSheet('游戏素材/img/enemy_left_sheet.png',(100,300))
#创建精灵组
group=pg.sprite.Group()
#把精灵添加到精灵组中
group.add(anima)
group.add(animaSheet)



isRunning=True
while isRunning:
    for ev in pg.event.get():
        if ev.type==pg.QUIT:
            isRunning=False
            break
        elif ev.type==pg.KEYDOWN:
            if ev.key==pg.K_SPACE:
                if animaSheet.y_index==0:
                    animaSheet.y_index=0
                    animaSheet.frame_count=3
                else:
                    animaSheet.y_index=0
                    animaSheet.frame_count=6
            elif ev.key==pg.K_LEFT:
                animaSheet.flip=True
                animaSheet.y_index = 0
                animaSheet.frame_count = 6
            elif ev.key==pg.K_RIGHT:
                animaSheet.flip=False
                animaSheet.y_index = 0
                animaSheet.frame_count = 6
        window.fill((227,227,227))

        # window.blit(image,rect)
        #
        # player.draw(window)
        group.draw(window)

        group.update()
        pg.display.update()
        clock.tick(60)#控制帧率



pg.quit()

