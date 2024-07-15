from .lib import * 
import os 

class CvBuilderWidget(SmoothScrollArea):


    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        with open("resources/packages.qss" , encoding='utf-8') as f : 
                    self.setStyleSheet( f.read() )
                    
        self.setObjectName(text.replace(' ', '-'))

        self.VBOX = QVBoxLayout(self)

        ## Frame1 
        self.frame1 = QFrame(self)
        self.VBOX.addWidget(self.frame1, 0 , Qt.AlignmentFlag.AlignTop)
        
        self.frame1_hbox = QHBoxLayout(self.frame1)
        self.TitleLabel = TitleLabel("Cv Builder", self.frame1)
        self.frame1_hbox.addWidget(self.TitleLabel)

        ## Frame 2 
        self.frame2 = QFrame(self)
        self.frame2_vbox = QHBoxLayout(self.frame2)

        self.VBOX.addWidget(self.frame2 , 1 , Qt.AlignmentFlag.AlignLeft )


        ### Frame 2 - 1 
        self.frame2_1 = QFrame(self.frame2)
        
        self.frame2_1_Hbox = QHBoxLayout(self.frame2_1)

        self.template1Label = BodyLabel("Template 1 : ", self.frame2_1)
        self.template1Link = HyperlinkButton(self.frame2_1)
        self.template1Button = TransparentPushButton("Launch", self.frame2_1)

        self.frame2_1_Hbox.addWidget(self.template1Label , 0 , Qt.AlignmentFlag.AlignLeft)
        self.frame2_1_Hbox.addWidget(self.template1Button, 0 , Qt.AlignmentFlag.AlignLeft)
        self.frame2_1_Hbox.addWidget(self.template1Link, 0 , Qt.AlignmentFlag.AlignCenter)

        self.template1Button.clicked.connect(self.updateServer)


        ## ADd Frame in Frame2 
        self.frame2_vbox.addWidget(self.frame2_1 , 0, Qt.AlignmentFlag.AlignLeft)
    

    def updateServer(self):
        self.template1Link.setText("Click")
        html_file_path = os.path.abspath("App/cvCreator1/index.html")
        self.template1Link.setUrl(QUrl(html_file_path))

        #print("Update/Launch Server")
        #self.worker = Worker1(self.template1Link , port=8001)
        #self.worker.finished.connect(self.handleServerUpdate)
        #self.worker.start()

    def handleServerUpdate(self, success):
        if success:
            return True
        else:
            self.template1Link.setUrl("")
            self.template1Link.setStyleSheet("color:red")


class Worker1(QThread):
    finished = pyqtSignal(bool)

    def __init__(self , hyperlink :HyperlinkButton , port ):
        super().__init__()
        # Configuration du serveur]
        self.port = port
        
        self.hyperlink = hyperlink

    def run(self):
        try:
            self.server_address = ('', self.port)  # Écoute sur le port 8001
            self.httpd = HTTPServer(self.server_address, CVServer1)
            # Obtenir l'adresse IP locale
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            self.hyperlink.setUrl(f"http://{local_ip}:{self.port}")
            self.hyperlink.setText(f"http://{local_ip}:{self.port}")

            print(f"http://{local_ip}:{self.port}")

            self.httpd.serve_forever()
            self.finished.emit(True)

        except Exception as e:
            self.finished.emit(False)



class CVServer1(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/App/cvCreator1/index.html'  # Nom du fichier HTML
        return super().do_GET()

