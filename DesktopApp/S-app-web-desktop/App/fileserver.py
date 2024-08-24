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
        self.mediaDirectory = create_media_folder()
        self.port = self.find_free_port()
        self.local_ip = self.get_local_ip()

        self.hyperlink=(f"http://{self.local_ip}:{self.port}")
        print("File Server init ....")

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Doesn't actually connect to 8.8.8.8, but tells the socket which interface to use
            s.connect(('8.8.8.8', 1))
            local_ip = s.getsockname()[0]
        except Exception:
            local_ip = '127.0.0.1'
        finally:
            s.close()
        return local_ip

    def find_free_port(self):
        port = 8000
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.bind(("", port))
                    return port
                except socket.error:
                    port += 1

    def launch(self , hyperlink) : 
        
        # Configuration du serveur
        server_address = ('', self.port)  # Écoute sur le port 8000
        httpd = HTTPServer(server_address, CustomHandler)
        print("Server launch")

        # Obtenir l'adresse IP locale


        
        print(f"Serving HTTP on http://{self.local_ip}:{self.port} from ..")

        # Démarrer le serveur
        httpd.serve_forever()



