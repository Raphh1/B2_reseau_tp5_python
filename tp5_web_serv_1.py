from http.server import BaseHTTPRequestHandler, HTTPServer
import time
 
hostName = "127.0.0.1"
serverPort = 8080
 
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>My Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello je suis un serveur HTTP</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
 
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))
 
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
 
    webServer.server_close()
    print("Server stopped.")