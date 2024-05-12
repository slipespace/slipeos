import http.server
import socketserver
import json
import subprocess

class CommandHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data)
            command = payload.get('command')
            if command:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                response = {'result': result.strip()}
                self._set_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                self._set_headers(400)
                self.wfile.write(json.dumps({'error': 'Missing command in request'}).encode('utf-8'))
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))

def run_server(port=8000):
    handler = CommandHandler
    with socketserver.TCPServer(('127.0.0.1', port), handler) as httpd:
        print(f'Server started on port {port}')
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
