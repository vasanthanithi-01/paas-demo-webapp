import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h2>Hello, PaaS Demo on Azure without Flask!</h2>")

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 8000))
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server running on http://0.0.0.0:{port}")
    httpd.serve_forever()