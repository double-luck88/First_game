import pygame as pg


#初始化pygame
pg.init()

#创建一个窗口,宽度800，高度600
window=pg.display.set_mode((800,600))

#设置窗口标题
pg.display.set_caption("hello pygame!")

#创建Clock对象,clock时钟意思
clock=pg.time.Clock()


img=pg.image.load('游戏素材/img/player_left_0.png')

#缩放图片
##缩放成指定大小
# new_img=pg.transform.scale(img,(100,100))
##缩放成原来的两倍
# new_img=pg.transform.scale2x(img)
##缩放成指定倍数
# new_img=pg.transform.scale_by(img,2)
# new_img=pg.transform.smoothscale_by(img,2)#平滑版本



#旋转图片
# new_img=pg.transform.rotate(img,45)

#旋转加缩放
# new_img=pg.transform.rotozoom(img,45,0.6)

#翻转
# new_img=pg.transform.flip(img,True,False)#左右翻转
# new_img=pg.transform.flip(img,True,True)#上下翻转

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
    window.blit(img,img.get_rect(center=(400-200,300)))
    window.blit(new_img,new_img.get_rect(center=(400,300)))



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