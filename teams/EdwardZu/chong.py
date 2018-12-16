import urllib.request
import time
while True:
    response = urllib.request.urlopen('http://172.20.10.12/num/index.html')
    file = response.read()
    print(file.decode('utf-8'))
    time.sleep(1)