import http.server
import socketserver
import json
import socket
from datetime import datetime
from qframelesswindow.webengine import FramelessWebEngineView
from PyQt5.QtCore import QUrl
import argostranslate.package
import argostranslate.translate
from json import load
import os
from urllib.parse import parse_qs
from PyQt5.QtWidgets import QFileDialog
import sys 

UPLOAD_DIR = "download"  
TRANSLATED_DIR = "download"  


class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.translator = Translator()  # Initialize the Translator class
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/api/packages':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            packages = [str(pkg) for pkg in argostranslate.package.get_installed_packages()]
            packages_split = [str(f).split(" → ") for f in packages]
            packages_from = list(set([str(f).split(" → ")[0] for f in packages]))
            packages_from_to = {package: [pack[1] for pack in packages_split if package == pack[0]] for package in packages_from}
            
            self.wfile.write(json.dumps(packages_from_to).encode())

        elif self.path == "/api/packages/settings/translator":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            packages = [str(pack).replace( "→" , "->") for pack in self.translator.installedPackages()]
            available = self.translator.availablesPackages()
            data = {"installed":packages , "availables":available}

            self.wfile.write(json.dumps(data).encode())

        else:
            super().do_GET()


    def do_POST(self):
        if self.path == '/api/translate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)

            from_language = data['from_language']
            to_language = data['to_language']
            if from_language != "" and to_language!="" : 
                text = data['text']

                if not self.translator.isLangInit or self.translator.from_lang.code != from_language or self.translator.to_lang.code != to_language:
                    self.translator.initLang(from_language, to_language)

                translated_text = self.translator.translate(text)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'translated_text': translated_text}).encode())
            else :
                pass


        elif self.path == "/api/packages/install":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            

            print("installong .... ", post_data)
            try:

                from_, to_ = data["package"].split(" -> ")
                self.translator.installLanguagesPackages(
                    from_language=from_,
                    to_language=to_
                )
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"installed": "true"}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"installed": "false", "error": str(e)}).encode())
                

        elif self.path == "/api/packages/remove":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            

            print("removing  .... ", data["package"].split(" -> "))
            try:
                
                from_, to_ = data["package"].split(" -> ")
                self.translator.uninstallPackage(
                    from_language=from_,
                    to_language=to_
                )
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"removed": "true"}).encode())
            except Exception as e:
                print(e)
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"removed": "false", "error": str(e)}).encode())
                

        elif self.path == "/api/translate/pdf":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            boundary = self.headers['Content-Type'].split("=")[1].encode()
            
            # Parse the form data
            parts = post_data.split(boundary)
            for part in parts:
                if b'Content-Disposition' in part:
                    headers, file_data = part.split(b'\r\n\r\n', 1)
                    headers = headers.decode()
                    if 'filename="' in headers:
                        filename = headers.split('filename="')[1].split('"')[0]
                        file_path = os.path.join(UPLOAD_DIR, filename)
                        with open(file_path, 'wb') as f:
                            f.write(file_data.strip(b'--\r\n'))
                        translated_file_path = self.translate_file(file_path)
                        response = {"path": translated_file_path}
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps(response).encode())

            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid request")


        else:
            self.send_response(404)
            self.end_headers()

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


    def translate_file(self, file_path):
        translated_file_path = os.path.join(TRANSLATED_DIR, "translated_" + os.path.basename(file_path))
        # Simuler le processus de traduction (copie simplement le fichier pour l'instant)
        os.system(f"cp {file_path} {translated_file_path}")
        
        print("Opening file dialog...")

        folder_path = os.path.dirname(translated_file_path)
        file_name = os.path.basename(translated_file_path)

        if sys.platform == 'win32':
            os.startfile(os.path.join(folder_path, file_name))
        elif sys.platform == 'darwin':
            os.system(f'open -R "{os.path.join(folder_path, file_name)}"')
        else:
            os.system(f'xdg-open "{folder_path}"')
        
        print("return file name \n")
        return file_name


class Translator:
    def __init__(self):
        self.isLangInit = False
        self.available_packages = argostranslate.package.get_available_packages()
        self.available_packages_list = sorted([ str(i).replace("→","->") for i in self.available_packages ] )


    def initLang(self, from_language, to_language):
        self.isLangInit = True
        with open("App/languages/codes.json", "r") as f:
            data = load(f)
            from_code = data[from_language]
            to_code = data[to_language]

        self.installed_languages = argostranslate.translate.get_installed_languages()
        self.from_lang = list(filter(
            lambda x: x.code == from_code,
            self.installed_languages))[0]

        self.to_lang = list(filter(
            lambda x: x.code == to_code,
            self.installed_languages))[0]

        self.translation = self.from_lang.get_translation(self.to_lang)

    def translate(self, text: str) -> str:
        return self.translation.translate(text)
    
    def installedPackages(self) :
        return argostranslate.package.get_installed_packages()


    def installLanguagesPackages(self , from_language , to_language) : 
        print("Updating package index ...")
        argostranslate.package.update_package_index()
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]
        
        print("Downloading Package ...")
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
        print("Downloaded and installed.")
        return True
    

    def availablesPackages(self) : 
        with open("App/languages/availables.json","r") as f:
            data = load(f)
        
        return list(data["Models"])


    def installLanguagesPackages(self , from_language , to_language) : 
        print("Updating package index ...")
        argostranslate.package.update_package_index()
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]
        
        print("Downloading Package ...")
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
        print("Downloaded and installed.")
        
    
    
    def uninstallPackage(self,from_language , to_language):
        with open("App/languages/codes.json" , "r") as f : 
            data = load(f) 
            from_code = data[from_language]
            to_code = data[to_language]

        available_package = list(filter(lambda x: x.from_code == from_code and x.to_code == to_code, self.available_packages))[0]   
             
        argostranslate.package.uninstall( available_package )




class Launcher:
    def __init__(self , parent=None) -> None:
        self.Handler = CustomHandler
        self.Handler.parent = parent

    # Fonction pour trouver un port libre
    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]
    
    def launch(self, port):
        # Essayer de démarrer le serveur sur plusieurs ports
        self.httpd = socketserver.TCPServer(("", port), self.Handler) 
        print(f"Serving on http://localhost:{port}")
        self.link = f"http://localhost:{port}"
        self.httpd.serve_forever()
