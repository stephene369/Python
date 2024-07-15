from .lib import *

class ReceiveWidget(SmoothScrollArea):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.Frame = QFrame(self)

        self.Frame_VBox = QVBoxLayout(self.Frame)
        self.Frame_VBox.setSpacing(20)

        with open("resources/receive.qss" , encoding='utf-8') as f : 
            self.setStyleSheet( f.read() )
        
        self.setObjectName(text.replace(' ', '-')) 
        self.Interface()


    def Interface(self)  :
        self.title = TitleLabel("Receive files : " , self.Frame)  
        self.Frame_VBox.addWidget(self.title)

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
        self.receiveConnection = PushButton(FIF.CONNECT, "Write the last number of the IP : ", self.frame2)
        self.lastOcterSpin = SpinBox(self.frame2)
        self.lastOcterSpin.setMaximum(1)
        self.lastOcterSpin.setMaximum(255)

        ## Frame3 
        self.receiveButton = PushButton(FIF.ACCEPT , "Receive",self.frame3)

        ### Adding object to frames 
        # frame 1
        self.Frame_VBox.addWidget(self.frame1)
        self.frame1.Hbox.addWidget(self.currentWifiLabel)
        self.frame1.Hbox.addWidget(self.currentWifiName)

        # frame 2
        self.Frame_VBox.addWidget(self.frame2)
        self.frame2.Hbox.addWidget(self.receiveConnection)
        self.frame2.Hbox.addWidget(self.lastOcterSpin)

        # frame 3
        self.Frame_VBox.addWidget(self.frame3)
        self.frame3.Hbox.addWidget(self.receiveButton)

        self.receiveButton.clicked.connect(self.getFiles)
  
        #self.lastOcterSpin.valueChanged.connect(self.getFiles)
        self.updateWifiName()


    def getFiles(self) : 
        self.Client = Client()
        host = self.get_local_ip_address()
        lastHoct = self.lastOcterSpin.value()
        host = ".".join((host.split(".")[:-1]))+f".{lastHoct}"
        print("The host  : " , host)

        self.Client.connection(
            host=host , parent=self
        )


    def updateWifiName(self) : 
        self.currentWifiName.setText(self.currentWifi())


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
