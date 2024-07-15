from .lib import *
from qfluentwidgets import InfoBar , dialog


class SendWidget(SmoothScrollArea):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.HBox = QHBoxLayout(self)

        self.Frame = QFrame(self)
        self.Frame.setObjectName("MainFrame")
        #self.Frame.setContentsMargins(20 , 20 , 20 , 0)
        self.HBox.addWidget(self.Frame)


        self.Frame_VBox = QVBoxLayout(self.Frame)
        #self.Frame_VBox.setSpacing(20)

        with open("resources/send.qss" , encoding='utf-8') as f : 
            self.setStyleSheet( f.read() )
        
        self.setObjectName(text.replace(' ', '-'))
        
        self.Interface()
        self.initButtonConnection()

    def Interface(self)  :
        self.title = TitleLabel("Send files or a Folder : " , self.Frame)        
        self.Frame_VBox.addWidget(self.title,0,
            Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        ## Creating frame 
        self.frame1 = HFrame(self.Frame)
        self.frame2 = HFrame(self.Frame)
        self.frame3 = HFrame(self.Frame)


        ## Creating object frame 
        ### Frame1
        self.currentWifiLabel = SubtitleLabel("Current Wifi : " , self.frame1)
        self.currentWifiName = SubtitleLabel("", self.frame2)
        self.qtimer = QTimer(self.frame1)
        self.qtimer.timeout.connect(self.updateWifiName)
        self.qtimer.start(1000)


        ## Frame2 
        self.receiveConnection = PushButton(FIF.CONNECT, "Accept connection : ", self.frame2)
        self.nbClientSpin = SpinBox(self.frame2)
        self.nbClientSpin.setMaximum(1)
        self.nbClientSpin.setMaximum(5)


        ## Frame3 
        self.sendFiles = PushButton(FIF.SEND_FILL,"Choose files to send",self.frame3)
        self.sendFolder = PushButton("Choose folders to send" , self.frame3)


        ### Adding object to frames 
        # frame 1
        self.Frame_VBox.addWidget(self.frame1)
        self.frame1.Hbox.addWidget(self.currentWifiLabel)
        self.frame1.Hbox.addWidget(self.currentWifiName)


        # frame 2
        self.Frame_VBox.addWidget(self.frame2)
        self.frame2.Hbox.addWidget(self.nbClientSpin)
        self.frame2.Hbox.addWidget(self.receiveConnection)

        # frame 3
        self.Frame_VBox.addWidget(self.frame3)
        self.frame3.Hbox.addWidget(self.sendFiles)
        self.frame3.Hbox.addWidget(self.sendFolder)


    def initButtonConnection(self) :
        self.receiveConnection.clicked.connect(self.receiveConnectionMethod)
        self.sendFiles.clicked.connect(self.sendFilesMethod)
        self.sendFolder.clicked.connect(self.sendFolderMethod)


    def sendFilesMethod(self) :
        if self.server.Clients : 
            self.server.get_file_settings(type_="files")
            self.server.send_settings()

    def sendFolderMethod(self):
        if self.server.Clients : 
            self.server.get_file_settings(type_="folder")
            self.server.send_settings()

        else : 
            self.createErrorInfoBar()


    def createErrorInfoBar(self): 
        InfoBar.error(
            title='Error',
            content="No client connected to the server ...",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=-1,    # won't disappear automatically
            parent=self.Frame )


    def receiveConnectionMethod(self):
        print("Worker Thread Accepting : ..  ")
        
        self.server = Server()
        self.nbClient = self.nbClientSpin.value()

        self.server.accept_connection(
            sock=self.server.sock ,
            nbclients=self.nbClient )
    

    def restartServer(self) : 
        pass 


    def updateWifiName(self) : 
        self.currentWifiName.setText(f"{self.currentWifi()} IP:{self.get_local_ip_address()}")

    def currentWifi(self) : 
        o_system = platform.system()
        if o_system == "Windows" :
            pass 
        elif o_system == "Linux":
            try :
                wifi_name = str(subprocess.check_output(['iwgetid'])).split(":")[1].replace("\\n","").replace('"',"").replace("\\","")
                return wifi_name
            
            except Exception as e :
                print(e)
                return None
    
    def get_local_ip_address(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("1.1.1.1", 1))
            ip_address = s.getsockname()[0]
        except Exception as e:
            print("Erreur lors de la récupération de l'adresse IP:", e)
            ip_address = ""
        finally:
            s.close()
        
        return ip_address 


class HFrame(QFrame) : 
    def __init__(self,parent=None) -> None:
        super().__init__(parent )

        self.Hbox = QHBoxLayout(self)

def get_local_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("1.1.1.1", 1))
        ip_address = s.getsockname()[0]
    except Exception as e:
        print("Erreur lors de la récupération de l'adresse IP:", e)
        ip_address = ""
    finally:
        s.close()
    
    return ip_address 

import socket
i = get_local_ip_address()

