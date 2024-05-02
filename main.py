import http.server
import socketserver

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World")

# 设置服务器端口
PORT = 8000

# 创建服务器对象
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
