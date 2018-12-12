from urllib import request
response = request.urlopen('http://192.168.142.132/person_num.html')
page = response.read().decode('utf-8')
print(page)
