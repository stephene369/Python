from Ui.library import *

class Acceuil :
    def __init__(self , parent:QWidget) :
        self.parent = parent 

    def setupUi(self) :
        self.PageAcceuil = QWidget()
        #self.PageAcceuil.setStyleSheet("background-color:rgba(32,32,32,72)")
        #self.PageAcceuil.setContentsMargins(0,0,60,0)
        #self.PageAcceuil.setSizeIncrement(QSize(80, 80))

        self.frame = QFrame(self.PageAcceuil)
        self.Vbox = QVBoxLayout(self.PageAcceuil)    
        self.Vbox.addWidget(self.frame,1,CENTER|CENTER)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
    ## frame
        self.label = QLabel(self.PageAcceuil,objectName='AccLab')
        self.button = QPushButton(self.PageAcceuil,objectName="AccBtn")
        self.Vbox2 = QVBoxLayout(self.frame)

        self.Vbox2.addWidget(self.label,0,CENTER|CENTER)
        self.Vbox2.addWidget(self.button,0,CENTER|BUTTOM )

        
        self.label.setText("""

                            Appliquez la stratégie des Moyennes Mobile ou la straégie combiné de l'Oscillateur Stochatique
                et de la Moyenne Mobile Convergence Divergence sur les données antérieurs des cours de clôture d'un actif fiinancier.\t
        Personnalisez chaque stratégie en fonction de votre objectif d'investissement, visionner les tendances, analyser les résultats, 
        choisisez les paramètres de votre stratégie de trading, prenez une decision.

        """)
       
    ## connection 

    ## 
        icon = QIcon("icons/download.svg")
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(30,30))
        self.button.setText("Charger un fichier 'csv'")

    ## 


#############
        return (self.PageAcceuil , self.button)



