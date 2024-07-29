import http.server
import socketserver
import json
import socket
from datetime import datetime

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


class Laucher : 
    def __init__(self) -> None:
        self.Handler = CustomHandler

    # Fonction pour trouver un port libre
    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]
    
    def lauch(self) : 
        # Essayer de démarrer le serveur sur plusieurs ports
        for port in range(8000, 8100):
            try:
                with socketserver.TCPServer(("", port), self.Handler) as httpd:
                    print(f"Serving on http://localhost:{port}")
                    httpd.serve_forever()
                    return f"http://localhost:{port}"
                
            except OSError as e:
                if e.errno == 98:  # Address already in use
                    print(f"Port {port} in use, trying another port...")
                else:
                    raise
