# A simple script in python to browse directory via a browser
# Author : @deekshithanand (Github)
import http.server
import socketserver
import webbrowser

PORT = 8888

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    webbrowser.open(f"localhost:{PORT}")
    try:
        httpd.serve_forever()
    except:
        print("Server Stopped!")
