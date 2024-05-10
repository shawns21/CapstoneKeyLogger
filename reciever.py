from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class NumberReceiver(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))
        number = payload.get('number')
        self._set_headers()
        self.log_number(number)

    def log_number(self, number):
        log_file = "numbers.log"
        with open(log_file, 'a') as f:
            f.write(f"Received number: {number}\n")

def run(server_class=HTTPServer, handler_class=NumberReceiver, port=1000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting number receiver server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
