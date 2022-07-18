import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import requests
import json
import base64
import os
#身份Key
apiKey = '你自己的key'
secretKey = '你自己的key'
#解析数据
def getToken():
    getTokenUrl = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+apiKey+'&client_secret='+secretKey
    response = requests.get(getTokenUrl)
    data = response.json()
    token = data.get('access_token')
    return token
# 创建函数getData
def getData():
    #地址
    url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'
    #图片编码
    with open(imagePath,'rb') as f:
        image = f.read()
    b64Image = base64.b64encode(image)
    print(b64Image)
    #获取车辆信息
    params = {'access_token':getToken()}
    data = {'image':b64Image}
    response = requests.post(url,params=params,data=data)
    content = response.json()
    result = content['result']
    print(result)
    #写入数据并跳转页面
    result = json.dumps(result)
    with open("file/info.txt",'w',encoding='utf-8') as f:
        f.write(result)
    window.destroy()
    #跳转到该目录的index2.py
    os.system('python index2.py')


#实现图片选择
def chooseImage():
    global imagePath
    imagePath = filedialog.askopenfilename(initialdir="./img",title='Choose an image.')
    carImg = ImageTk.PhotoImage(file=imagePath)
    car = tk.Label(window,width=367,height=275,image=carImg)
    car.place(x=185,y=160)
    window.mainloop()

#创建窗口绘制背景
window = tk.Tk()
window.geometry('1000x600') #窗口默认大小
window.resizable(0,0) #锁定窗口大小改变
window.title('车型识别') #窗口标题
bgImg = ImageTk.PhotoImage(file="images/bg1.jpg")
bg = tk.Label(window,width=1000,height=600,image=bgImg)
bg.pack()
#添加选择图片按钮
selectImg = ImageTk.PhotoImage(file="images/select.jpg")
select = tk.Button(window,image=selectImg,bd=0,width=192,height=63,command=chooseImage)
select.place(x=750,y=180)
#添加开始识别按钮
okImg = ImageTk.PhotoImage(file="images/ok.jpg")
ok = tk.Button(window,image=okImg,bd=0,width=192,height=63,command=getData)
ok.place(x=750,y=400)

window.mainloop()
