from http.server import SimpleHTTPRequestHandler, HTTPServer
import socket

class CVServer(SimpleHTTPRequestHandler):
    # Redéfinition de la méthode do_GET pour servir cv_creator.html
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Nom du fichier HTML
        return super().do_GET()

# Configuration du serveur
server_address = ('', 8000)  # Écoute sur le port 8000
httpd = HTTPServer(server_address, CVServer)

# Obtenir l'adresse IP locale
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Serving CV Creator on http://{local_ip}:8000...")

# Démarrer le serveur
httpd.serve_forever()
