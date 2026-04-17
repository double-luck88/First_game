import pygame as pg


#初始化pygame
pg.init()

#创建一个窗口,宽度800，高度600
window=pg.display.set_mode((800,600))

#设置窗口标题
pg.display.set_caption("hello pygame!")

#设置窗口背景颜色,RGE
#window.fill((217,217,217))
#window.fill('red')
window.fill(pg.Color(227,227,227))
#////////////////在这里放置绘图代码//////////////////



#/////////////////////////////////////////////////


#更新窗口
pg.display.update()

#暂停一会窗口,5000=5s
pg.time.wait(5000)


#清理，退出pygame
pg.quit()