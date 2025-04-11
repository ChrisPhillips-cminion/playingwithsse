
import http.server
import socketserver
import time

class SSERequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()

            while True:
                event = {"data": f"Event {time.time()}"}
                self.wfile.write(f"data: {event}\n\n".encode())
                time.sleep(1)

PORT = 8000

with socketserver.TCPServer(("", PORT), SSERequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
