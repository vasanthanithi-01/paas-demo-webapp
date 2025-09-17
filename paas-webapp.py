from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, PaaS Demo on Azure without Flask!")

httpd = HTTPServer((host, port), MyHandler)
print(f"Server running on http://{host}:{port}")
httpd.serve_forever()
