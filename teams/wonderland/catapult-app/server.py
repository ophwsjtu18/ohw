import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)
ser = None

for p in ports:
    print(p[1])
    if "Arduino" in p[1]:
        ser = serial.Serial(port=p[0])

if ser == None:
    print("No Arduino Device was found connected to the computer")
    exit(0)

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 9999

ser.write(b'B140')

base_position = 140
current_state = 0

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        paths = {
            '/': {'status': 200},
            '/base/right': {'status': 200},
            '/base/left': {'status': 200},
            '/state/1': {'status': 200},
            '/state/2': {'status': 200},
            '/state/0': {'status': 200},
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        global base_position
        global current_state

        print(path)

        self.send_response(status_code)
        if path != '/':
            self.send_header('Content-type', 'application/json')

        self.end_headers()
        if path == '/':
            f = open('index.html', 'r')
            content = f.read()
            f.close()
        elif path == '/base/right':
            new_p = max(20, base_position - 30)
            base_position = new_p
            ser.write(('B%s' % new_p).encode('utf-8'))
            content = json.dumps({
                'current_position': base_position
            })

        elif path == '/base/left':
            new_p = min(160, base_position + 30)
            base_position = new_p
            ser.write(('B%s' % new_p).encode('utf-8'))
            content = json.dumps({
                'current_position': base_position
            })

        elif path == '/state/0':
            current_state = 0
            ser.write((str(current_state)).encode('utf-8'))
            content = json.dumps({
                'current_state': current_state
            })

        elif path == '/state/1':
            current_state = 1
            ser.write((str(current_state)).encode('utf-8'))
            content = json.dumps({
                'current_state': current_state
            })

        elif path == '/state/2':
            current_state = 2
            ser.write((str(current_state)).encode('utf-8'))
            content = json.dumps({
                'current_state': current_state
            })

        print(content)
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
