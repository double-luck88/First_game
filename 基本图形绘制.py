import pygame as pg


#初始化pygame
pg.init()

#创建一个窗口,宽度800，高度600
window=pg.display.set_mode((800,600))

#设置窗口标题
pg.display.set_caption("hello pygame!")

#设置窗口背景颜色,RGE
window.fill((217,217,217))
#window.fill('red')
# window.fill(pg.Color(227,227,227))


#////////////////在这里放置绘图代码//////////////////




#绘制线50->开始坐标，150->结束坐标,5->线的粗细
#aaline抗锯齿，5->是颜色混色程度；blend为0时混合度为零
# pg.draw.line(window,'red',(50,50),(150,150),5)
# pg.draw.aaline(window,'red',(50,50),(150,150),1)

points=[(50,50),(50,180),(200,100)]

#绘制多条线,True是把开始点和结束点连接起来，用False就不会连接
# pg.draw.lines(window,'green',True,points)
# pg.draw.aalines(window,'green',True,points)

#绘制多边形,polygon三角形
# pg.draw.polygon(window,'red',points,5)

#绘制矩形
# pg.draw.rect(window,'blue',(50,50,150,35))    #填充矩形
# pg.draw.rect(window,'blue',(50,100,150,35),2)    #非填充矩形
# pg.draw.rect(window,'blue',(50,150,150,35),2,15)    #非填充矩形,绘制圆角，15是圆角半径
# pg.draw.rect(window,'blue',(50,200,150,35),0,15)    #width=0，填充矩形,绘制圆角；
# pg.draw.rect(window,'blue',(50,200,150,35),0,50,10,50,10)    #填充矩形,绘制圆角；width=0;四个角的不同的圆角半径

#绘制园
##正圆
# pg.draw.circle(window,'blue',(400,300),50)  #50半径.填充园
# pg.draw.circle(window,'blue',(400,300),50,width=1)  #50半径，不填充
# pg.draw.circle(window,'blue',(400,300),50,width=1,draw_top_left=True)  #50半径,只绘制左上角

##椭圆
# pg.draw.ellipse(window,"red",(0,0,200,200),width=5)

#绘制弧线
pg.draw.arc(window,'red',(0,0,150,40),0,1.562)  #150宽度40高度，0是开始弧度，1.562是派的一半,是结束的弧度




#/////////////////////////////////////////////////


#更新窗口
pg.display.update()

#暂停一会窗口,5000=5s
pg.time.wait(5000)


#清理，退出pygame
pg.quit()