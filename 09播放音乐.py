import pygame as pg
import os

pg.init()
pg.mixer.init()

pg.display.set_mode((800,600))
print("music 文件夹下真实内容：",os.listdir('music'))

#设置音乐播放完成后，触犯的事件
##自定义一个事件
MUSIC_END=pg.USEREVENT+1
##把这个事件注册到pycharm
pg.mixer.music.set_endevent(MUSIC_END)

mus_list=[
    'music/Wish_You_Were_Here_-_the.madpix.project.mp3',#一定要记得这里加‘逗号’啊
    'music/古风轻快氛围 调皮可爱 by 蜡笔小嘉-完整版.mp3',
    'music/轻音乐钢琴婚礼-浪漫抒情-千年之恋_爱给网_aigei_com.mp3'
    #'D:\pythonProject2\music\Wish_You_Were_Here_-_the.madpix.project.mp3'
]
current_index=0

def next_mus():
    global current_index
    # 播放下一首
    current_index += 1
    # 循环播放
    if current_index==len(mus_list):
        current_index=0
    pg.mixer.music.load(mus_list[current_index])
    pg.mixer.music.play()

def prev_mus():
    global current_index
    # 播放上一首
    current_index -= 1
    # 循环播放
    if current_index<0:
        current_index=len(mus_list)-1
    pg.mixer.music.load(mus_list[current_index])
    pg.mixer.music.play()


# #加载音乐
pg.mixer.music.load('music/Wish_You_Were_Here_-_the.madpix.project.mp3')

#播放音乐
pg.mixer.music.play(0,260)
#pg.mixer.music.play(0,60,5000)#60是从60s开始播放，5000是毫秒等于5s意思音量从小到5s恢复正常



isRunning=True
while isRunning:
    for ev in pg.event.get():
        if ev.type==pg.QUIT:
            isRunning=False
            break
        elif ev.type==MUSIC_END:
            print('music end')
            # #播放下一首
            # current_index+=1
            # #循环播放
            # if current_index==len(mus_list):
            #     current_index=0
            # pg.mixer.music.load(mus_list[current_index])
            # pg.mixer.music.play()
            next_mus()#函数封装后得加上
            pass
        elif ev.type==pg.KEYDOWN:
            #空格控制播放、暂停音乐
            if ev.key==pg.K_SPACE:
                print(f"按下了键：{ev.key}")
                #如果在播放
                if pg.mixer.music.get_busy():
                    #暂停播放
                    pg.mixer.music.pause()
                else:
                    #恢复播放
                    pg.mixer.music.unpause()
            #按s停止播放
            elif ev.key==pg.K_s:#注意：按s键或其他时要用英文输入法否则没反应
                print("进入s键分支")
                pg.mixer.music.stop()
            #从头开始播放
            elif ev.key==pg.K_r:
                pg.mixer.music.rewind()
            #调大音量
            elif ev.key==pg.K_UP:
                #获取当前音量[0,1]
                volume=pg.mixer.music.get_volume()
                #++
                pg.mixer.music.set_volume(volume+0.05)
            elif ev.key==pg.K_DOWN:
                #获取当前音量[0,1]
                volume=pg.mixer.music.get_volume()
                #++
                pg.mixer.music.set_volume(volume-0.05)
            #用左右键控制上下首歌
            elif ev.key==pg.K_LEFT:
                prev_mus()
            elif ev.key==pg.K_RIGHT:
                next_mus()


pg.quit()