from urllib import request
response = request.urlopen('http://10.163.126.35/person_num.html') 
#桥接模式设置虚拟机，复制物理网络连接状态，ipconfig，填入ip地址

page = response.read().decode('utf-8')
print(page)
