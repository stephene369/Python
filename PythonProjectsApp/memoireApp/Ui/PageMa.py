from Ui.library import *

class Page2 :
    def __init__(self , parent:QWidget) :
        self.parent = parent 
        self.ScrollArea = QScrollArea(self.parent)
        self.page = QWidget(self.ScrollArea)

        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setWidget(self.page)
        
    def setupUi(self) :
        self.page.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.VBox = QVBoxLayout(self.page)

        self.frame0 = QFrame(self.page)
        self.frame1 = QFrame(self.page)
        self.button = QPushButton(self.page)
        self.frame1.setObjectName("Frame1")

        self.VBox.addWidget(self.frame0,0,LEFT|VCENTER)
        self.VBox.addWidget(self.frame1,0,CENTER|VCENTER)
        self.VBox.addWidget(self.button,0,HCENTER|VCENTER)
        self.frame1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.frame1.setStyleSheet("background-color: red  ")

        self.button.setContentsMargins(0,0,0,0)
        self.button.setText("Commencer les Simulations")
        ### Frame 0 
        self.VBox = QVBoxLayout(self.frame0)
        self.label1 = QLabel(self.frame0,objectName="labMaTitle")
        self.label1.setText("Moving Average Strategy")
        self.VBox.addWidget(self.label1,0,HCENTER|TOP)
        

        ### FRame  1 
        #self.frame1.setMinimumHeight(400)

        self.Hbox0 = QHBoxLayout(self.frame1)
        self.frame0 = QFrame(self.frame1)
        self.frame0.setObjectName("profilFrame" )
        self.frame1 = QFrame(self.frame1)
        self.frame1.setObjectName("parameterFrame")

        self.Hbox0.addWidget(self.frame0,0,LEFT|CENTER)
        self.Hbox0.addWidget(self.frame1,0,RIGHT|CENTER)

## Franme 0 Profil 
        self.VBox =  QVBoxLayout(self.frame0)
        self.label = QLabel(self.frame0 , objectName="maProfilTitle")
        self.label.setText("Déterminer votre profil d'investisseur")
        self.VBox.addWidget(self.label , 0 , 
        Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop )
        
            ## grid Profil investisseur
        self.grid = QGridLayout(self.frame0)
        
        self.maProfilAddWidget(items=["Croissance de Capital","Speculation ", "Protection du Patrimoine " ,
        "Revenu Régulier " ,"Autres "] ,
        grid=self.grid,frame=self.frame0,labText="Objectif d'investissement",
        keys="objectif")
        
        self.maProfilAddWidget(items=["Court terme","Moyen terme" , "Long terme"] ,
        grid=self.grid,frame=self.frame0,labText="Horizon temporel",
        keys="horizon")

        self.maProfilAddWidget(items=["Prudent","Modere","Energétique"] ,
        grid=self.grid,frame=self.frame0,labText="Tolérance au Risque",
        keys="tolerance")

        self.grid.setContentsMargins(0,0,0,0)
        self.VBox.addLayout(self.grid,1 )

### Frame Parameters --------------------------------

        self.VBox = QVBoxLayout(self.frame1)
        self.label = QLabel(self.frame1)
        self.label.setText("Paramètres")
        self.label.setObjectName("maProfilTitle")
        self.VBox.addWidget(self.label,0,HCENTER|TOP)
        

        self.grid = QGridLayout(self.frame1)
        self.maParameterAddWidget(grid=self.grid,keys='courte',
            parent=self.frame1,labText="Fenêtre Courte" , 
        infos="Nombre de périodes utilisées pour calculer une moyenne mobile courte.\nCe choix dépendra de votre stratégie de trading, de votre horizon d'investissement")
        self.maParameterAddWidget(grid=self.grid,keys='longue',
            parent=self.frame1,labText="Fenêtre Longue", 
        infos="nombre de périodes utilisées pour calculer une moyenne mobile Longue.\nCe choixdépendra de votre stratégie de trading, de votre horizon d'investissement")
        
        ### ADDING GRID TO FRAME ###
        self.grid.setContentsMargins(0,0,0,0)
        self.VBox.addLayout(self.grid,1)
        self.grid

        with open("style/ma.scss",'r') as style :
            style = style.read()
            self.page.setStyleSheet(style)


        return self.ScrollArea , self.button
    
    def maProfilAddWidget(self , items:list , keys:str , grid:QGridLayout ,  
                frame:QFrame , labText:str ) :

        self.label = QLabel(frame)
        self.label.setText(labText)
        self.label.setObjectName("MaProfilLabel")
        
        self.Combo = QComboBox(frame)
        self.Combo.setObjectName("MaProfilCombo")
        self.Combo.addItems(items)
        self.Combo.setFixedHeight(self.Combo.height()*1 )
        self.Combo.setFixedWidth(self.Combo.width()*3  )

        #if not keys in OBJECT.keys() :
        #   OBJECT[keys] = ''
        OBJECT[keys] = self.Combo

        i=grid.rowCount()
        grid.addWidget(self.label,i+1,0,1,1,
        Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)
        grid.addWidget(self.Combo,i+2,0,1,1,
        Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)        
        
        self.sizePolic = QSizePolicy(QSizePolicy.Policy.Expanding , 
        QSizePolicy.Policy.Fixed )
        #self.Combo.setSizePolicy(self.sizePolic)


    def maParameterAddWidget(self , grid:QGridLayout,keys:str,parent:QFrame,
                    labText:str , infos:str) :

        self.label = QLabel(parent , objectName ="MaParametreLab" )
        self.spin1 = QSpinBox(parent,objectName = "MaParametreSpin")
        self.spin2 = QSpinBox(parent,objectName = "MaParametreSpin")
        self.info = QLabel(parent,objectName = "infoLab")
        for OBJ in  [self.spin1,self.spin2] :
            OBJ.setFixedHeight( OBJ.height()*1 )
            OBJ.setFixedWidth( OBJ.width()*1.6  )
            OBJ.setMinimum(2)
            OBJ.setMaximum(200)

        self.label.setText(labText)
        self.info.setText(infos)
        
        i = grid.rowCount()
        grid.addWidget(self.label,i+1,0,1,2,LEFT|BUTTOM)
        grid.addWidget(self.info,i+2,0,1,2,LEFT|BUTTOM)
        grid.addWidget(self.spin1,i+3,0,1,1,LEFT|TOP)
        grid.addWidget(self.spin2,i+3,1,1,1,LEFT|TOP)

        OBJECT[keys] = [self.spin1 , self.spin2]

    def fonction(self , nb) :
        from time import sleep
        print("Debut")
        self.spin1.setValue(100)
        for i in range(3,12) : 
            self.spin2.setValue(i)
            sleep(1)
        self.nb = nb
        return nb
    
    def exec (self) :
        print("Debut")
        with ThreadPoolExecutor() as executor :
            program = executor.submit(self.fonction , nb=12)
            
        print("fin")
        self.resultat = program.result()
        print(self.resultat)


    def para(self) :
        from threading import Thread
        thread = Thread(target=self.fonction , args=[12])
        thread.start()





        