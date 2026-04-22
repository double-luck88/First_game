import pygame as pg


#初始化pygame
pg.init()

#创建一个窗口,宽度800，高度600
window=pg.display.set_mode((800,600))

#设置窗口标题
pg.display.set_caption("hello pygame!")

#创建Clock对象,clock时钟意思
clock=pg.time.Clock()

#设置按键重复
pg.key.set_repeat(1,16)

x,y=0,0

#游戏主循环（不断处理用户输入）
isRunning=True
while isRunning:
    #处理事件
    for ev in pg.event.get():
        #退出事件，当你点击右上角的X
        if ev.type==pg.QUIT:
            isRunning =False
            break
        #键盘按下事件
        '''
        elif ev.type==pg.KEYDOWN:
             # 是什么键按下了
             if ev.key==pg.K_UP:
                 y-=5
             elif ev.key==pg.K_DOWN:
                 y+=5
             elif ev.key==pg.K_LEFT:
                 x-=5
             elif ev.key==pg.K_RIGHT:
                 x+=5

        '''

    #获取当前的键
    keys=pg.key.get_pressed()
    #判断某个键是否按下了
    if keys[pg.K_UP]:
        y-=5
    if keys[pg.K_DOWN]:
        y+=5
    if keys[pg.K_LEFT]:
        x-=5
    if keys[pg.K_RIGHT]:
        x+=5



    #设置窗口背景颜色,RGE(0~255)
    #window.fill((217,217,217))
    #window.fill('red')
    window.fill(pg.Color(227,227,227))


    #////////////////在这里放置绘图代码//////////////////

    # pg.draw.rect(window,(255,255,0),(20,20,50,50))#前面时颜色，后面括号前面两个是坐标x,y，后面是大小
    pg.draw.rect(window,(255,255,0),(x,y,50,50))#前面时颜色，后面是大小
    # x+=1
    # y+=1

    #/////////////////////////////////////////////////


    #更新窗口
    pg.display.update()

    #获取当前帧率
    # print(f"framerate is {clock.get_fps()}")

    #设置帧率
    clock.tick(60)

print('hello')


#清理，退出pygame
pg.quit()
