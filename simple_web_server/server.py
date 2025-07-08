import http.server
import socketserver
import os

PORT = 8000
WEB_DIR = os.path.dirname(os.path.abspath(__file__)) # Serve files from the script's directory

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Serving files from: {WEB_DIR}")
    print(f"Open http://localhost:{PORT}/ to view the website.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
