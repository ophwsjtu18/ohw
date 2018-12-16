import urllib.request as request
import time
url = "http://192.168.50.144/num/index.html"
# 其中具体ip地址要视网络热点决定（寝室192.168.50.144）

while True:
    file = request.urlopen(url)
    dataline = file.readline()
    print(dataline.decode("utf-8"))
    time.sleep(1)
    # print(type(dataline)) #读取为bytes形式，需要decode（）
