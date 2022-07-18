import pygame
import json
pygame.init()

#创建窗口绘制背景
canvas = pygame.display.set_mode((1000,600))
pygame.display.set_caption('车型识别') #pygame窗口标题
bg = pygame.image.load("images/bg2.jpg") #加载图片
canvas.blit(bg,(0,0)) #图片布局
#读取数据
with open('file/info.txt','r',encoding='utf-8')as f:
    cars = f.read()
cars = json.loads(cars)
print(type(cars))

def fillText(content,pos):
    font = pygame.font.Font("font/simhei.ttf",20)
    text = font.render(content,True,(255,255,255))
    canvas.blit(text,pos)

#请在下方书写你的代码
names = []
scores = []
for i in cars:
    names.append(i['name'])
    scores.append(int(i['score']*100))
print(names)
print(scores)

def showInfo(n,s):
    y = 220
    for index in range(len(n)):
        fillText(n[index],(230,y))
        fillText(str(s[index]),(690,y))
        if s[index] != 0:
            pygame.draw.rect(canvas,(255,255,255),(485,y,s[index],10),0)
        y+=60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #请在下方书写你的代码
    showInfo(names,scores)
    #刷新窗口
    pygame.display.update()



        

