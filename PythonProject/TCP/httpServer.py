import http.server
import socketserver

# Spécifiez les numéros de port et les noms de fichiers à servir
PORT = 2003
IpLocal = "192.168.1.125"


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=r"C:\Users\Stephn\Downloads\Le Brio (2017) [720p] [BluRay] [YTS.MX]", **kwargs)

# Créez un serveur web avec le gestionnaire personnalisé

with socketserver.TCPServer((IpLocal,PORT), MyHandler) as httpd:
    print(f"Serveur actif sur le port {PORT}... ")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")


