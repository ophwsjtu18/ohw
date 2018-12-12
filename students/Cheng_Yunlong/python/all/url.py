import urllib.request
while True:
    response = urllib.request.urlopen('http://192.168.40.130')
    html = response.read()
    html
