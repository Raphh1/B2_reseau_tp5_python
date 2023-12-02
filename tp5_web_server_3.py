from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "127.0.0.1"
serverPort = 8080
baseDirectory = "htdocs"  # le répertoire contenant les fichiers HTML

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        file_path = os.path.join(baseDirectory, self.path[1:])

        # Si le fichier demandé existe, renvoie son contenu
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
        else:
            # Sinon, renvoie une réponse 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>404 Not Found</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>404 Not Found</p></body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
