from urllib import request
import time
while(True):
	f = request.urlopen("http://192.168.209.138/data.html")
	data = f.read()
	data = data.decode('utf-8')
	data = data.split('\n')
	print("diff in x axis is " + str(float(data[0])*100) + "%")
	print("diff in y axis is " + str(float(data[1])*100) + "%")
	time.sleep(5)
