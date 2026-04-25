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
#2.相对路径，相对于py文件来说。
img=pg.image.load('游戏素材/img/player_left_0.png')#.convert()

#设置透明色
img.set_colorkey('white')

#使用png透明图片
pig_img=pg.image.load('游戏素材/img/enemy_right_1.png')#.convert_alpha()
#pig_img=pg.image.load('游戏素材/img/enemy_right_1.png').corvert_alph()

#自己创建透明图片，然后自己在图片上绘图
draw_img=pg.Surface((200,200),pg.SRCALPHA)#200大小,创建的图片大小
pg.draw.rect(draw_img,'red',(50,50,100,100))#在图片上绘制一个矩形
pg.draw.rect(draw_img,'blue',draw_img.get_rect(),1)#描绘矩形边框


x,y=0,0
alpha=255 #255就是完全不透明
direction=-1

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
    #window.fill('green')
    window.fill(pg.Color(227,227,227))


    #////////////////在这里放置绘图代码//////////////////

    #绘制图片
    # window.blit(img,(x,y),None) #None也可以不写
    window.blit(img,(0,0))
    window.blit(img,(img.get_width(),0),(0,0,84,91))#对图片进行裁剪
    window.blit(pig_img,pig_img.get_rect(center=(400,500)))
    #动态修改图片透明度（0~255）
    draw_img.set_alpha(alpha)
    window.blit(draw_img,(0,250))
    # x+=1
    # y+=1

    #产生渐变的效果
    #alpha=255 if alpha==-1 else alpha-1 #alpha等于-1就等于255否则就减1

    alpha+=direction
    if alpha<=0:
        alpha=0
        direction=1
    elif alpha>=255:
        alpha=255
        direction=-1




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