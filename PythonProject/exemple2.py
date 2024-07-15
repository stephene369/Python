import http.server
import socketserver
import sys
import os

# Choisissez le répertoire à partir duquel le serveur sera lancé
repertoire_serveur = r'C:\Users\Stephn\Videos'

# Choisissez le port sur lequel le serveur écoutera
port_serveur = 2003

# Se déplacer dans le répertoire du serveur
try:
    os.chdir(repertoire_serveur)
except FileNotFoundError:
    print(f"Le répertoire {repertoire_serveur} n'existe pas. Veuillez le vérifier.")
    sys.exit(1)

# Configurer le gestionnaire de requêtes
handler = http.server.SimpleHTTPRequestHandler

# Utiliser 0.0.0.0 comme adresse pour écouter sur toutes les interfaces réseau
adresse = "198.168.0.210"

# Démarrer le serveur
with socketserver.TCPServer((adresse, port_serveur), handler) as httpd:
    print(f"Serveur lancé sur http://{adresse}:{port_serveur}/")
    print("Le serveur est accessible depuis d'autres appareils sur le même réseau.")

    # Attendre les requêtes
    httpd.serve_forever()
