import requests, json
r = requests.get('http://192.168.1.28:9000/')
data = json.loads(r.content)
if 'person' in data:
    print(data['person'])
else:
    print('No person found.')