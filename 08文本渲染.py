import pygame as pg

pg.init()

window=pg.display.set_mode((800,600))

#文本
text="hello Pygame"
#把文本渲染成Surface
##1，获取系统字体（只支持英文，不支持中文）
font=pg.font.Font(None,36)
#font=pg.font.SysFont(None,36)#用这个版本不兼容

font.set_bold(True)#是否粗体
font.set_italic(True)#斜体
font.set_strikethrough(True)#删除线
font.set_underline(True)#下划线

##2,用font来渲染文本
# text_img=font.render(text,False,'red')#用False字体表面凹凸不平
text_img=font.render(text,True,'red','yellow')

##1.打开中文字体
#在系统c盘window找到fonts把字体复制到pycharm里，'\'记得改成'/'
chinese_font=pg.font.Font('游戏素材/fonts/STXINGKA.TTF',36)
chinese_img=chinese_font.render('你好 Pygame',True,'red')

isRunning=True
while isRunning:
    for ev in pg.event.get():
        if ev.type==pg.QUIT:
            isRunning=False
            break

    window.fill((227,227,227))
    window.blit(text_img,(0,0))
    window.blit(chinese_img,(0,50))

    pg.display.update()
pg.quit()