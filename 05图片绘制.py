import pygame as pg


#初始化pygame
pg.init()

#创建一个窗口,宽度800，高度600
window=pg.display.set_mode((800,600))

#设置窗口标题
pg.display.set_caption("hello pygame!")

#创建Clock对象,clock时钟意思
clock=pg.time.Clock()

#加载图片
#1.绝对路径，带盘符的路径。一般不用这个
# img=pg.image.load('D:\pythonProject2\游戏素材\img\player_left_0.png')
#相对路径，相对于py文件来说。
img=pg.image.load('游戏素材/img/player_left_0.png')


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

    #设置窗口背景颜色,RGE(0~255)
    #window.fill((217,217,217))
    #window.fill('red')
    window.fill(pg.Color(227,227,227))


    #////////////////在这里放置绘图代码//////////////////

    #绘制图片
    # window.blit(img,(x,y),None) #None也可以不写
    window.blit(img,(0,0))
    window.blit(img,(img.get_width(),0),(0,0,84,91))#对图片进行裁剪



    x+=1
    y+=1

    #/////////////////////////////////////////////////


    #更新窗口
    pg.display.update()

    #获取当前帧率
    print(f"framerate is {clock.get_fps()}")

    #设置帧率
    clock.tick(60)

print('hello')


#清理，退出pygame
pg.quit()