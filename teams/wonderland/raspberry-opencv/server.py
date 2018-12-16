import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST_NAME = '172.20.10.2'
PORT_NUMBER = 9000


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        paths = {
            '/': {'status': 200},
            '/bar': {'status': 302},
            '/baz': {'status': 404},
            '/qux': {'status': 500}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        f = open('objects.json', 'r')
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content = f.read()
        f.close()
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
