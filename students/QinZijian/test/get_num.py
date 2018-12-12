import time
from urllib import request
while True:
    response = request.urlopen('http://192.168.1.101/cmd.html') 
    #桥接模式设置虚拟机，复制物理网络连接状态，ipconfig，填入ip地址

    page = response.read().decode('utf-8')
    print(page)
    time.sleep(0.2)
