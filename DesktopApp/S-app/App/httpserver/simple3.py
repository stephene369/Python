from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path
import socket
import json
from qfluentwidgets import HyperlinkButton

def create_media_folder():
    home_dir = Path.home()
    downloads_dir = home_dir / "Downloads"
    media_dir = downloads_dir / "media"
    
    if not media_dir.exists():
        media_dir.mkdir(parents=True)

    return media_dir



class CustomHandler(SimpleHTTPRequestHandler):
    # Créer le dossier media
    media_dir = create_media_folder()

    # Définir le chemin du fichier index.html
    current_dir = Path(__file__).parent
    index_file = current_dir / "index.html"

    def translate_path(self, path):
        # Définir le chemin racine pour servir les fichiers
        path = super().translate_path(path)
        relpath = Path(path).relative_to(Path.cwd())
        return str(self.media_dir / relpath)

    def convert_bytes(self, bytes):
        # Convertir en Mo ou Go
        if bytes < 1024 * 1024 * 1024:  # Moins de 1 Go
            megabytes = bytes / (1024 * 1024)
            return f"{round(megabytes, 2)} Mo"
        else:  # 1 Go et plus
            gigabytes = bytes / (1024 * 1024 * 1024)
            return f"{round(gigabytes, 2)} Go"

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            self.serve_index()
        elif self.path == '/files':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            file_list = []
            for f in self.media_dir.iterdir():
                if f.is_file():
                    size_in_bytes = f.stat().st_size
                    size_formatted = self.convert_bytes(size_in_bytes)
                    file_list.append({"name": f.name, "size": size_formatted, "url": f"/{f.name}"})
            self.wfile.write(json.dumps({"files": file_list}).encode())
        else:
            return super().do_GET()

    def serve_index(self):
        try:
            with open(self.index_file, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        except Exception as e:
            self.send_error(404, f"File not found: {self.path}")

    def end_headers(self):
        if not self.path.endswith('/index.html') and not self.path.endswith('/files'):
            self.send_header('Content-Disposition', 'attachment')
        super().end_headers()

class FileServer :
    def __init__(self) :
        print("File Server init ....")

    def launch(self , hyperlink:HyperlinkButton=None) : 
        port = 7999
        
        # Configuration du serveur
        server_address = ('', 7999)  # Écoute sur le port 8000
        httpd = HTTPServer(server_address, CustomHandler)
        print("Server launch")

        # Obtenir l'adresse IP locale
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        

        if hyperlink:
            hyperlink.setUrl(f"http://{local_ip}:{port}")
            hyperlink.setText(f"http://{local_ip}:{port}")
        print(f"Serving HTTP on http://{local_ip}:{port} from ..")

        # Démarrer le serveur
        httpd.serve_forever()





