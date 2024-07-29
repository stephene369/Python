import http.server
import socketserver
import json
import socket
from datetime import datetime
from qframelesswindow.webengine import FramelessWebEngineView
from PyQt5.QtCore import QUrl

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/run-python-code':
            self.run_python_code()
        else:
            super().do_GET()

    def run_python_code(self):
        # Le code Python que tu veux exécuter
        result = "Python code executed successfully!"
        
        # Préparer la réponse
        response = {
            "message": result + str(datetime.now())
        }
        
        # Envoyer la réponse
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


class Launcher : 
    def __init__(self) -> None:
        self.Handler = CustomHandler

    # Fonction pour trouver un port libre
    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]
    
    def lauch(self , port) : 
        # Essayer de démarrer le serveur sur plusieurs ports
        self.httpd = socketserver.TCPServer(("", port), self.Handler) 
        print(f"Serving on http://localhost:{port}")
        self.link = f"http://localhost:{port}"
        self.httpd.serve_forever()
    
