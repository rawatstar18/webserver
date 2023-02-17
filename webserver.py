import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Serving at port', PORT)
    httpd.serve_forever()

