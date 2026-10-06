from http.server import BaseHTTPRequestHandler, HTTPServer

def add(a, b):
    return a + b

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"2 + 3 = {add(2, 3)}\n".encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
