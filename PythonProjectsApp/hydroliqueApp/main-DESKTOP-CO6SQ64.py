from interfaces.Ui_hydro import *
from startup.start import *
import json
from numpy import inf

class MainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ##
        self.setGeometry(int(WIDTH_/11), int(HEIGHT_ / 11), int(WIDTH_ / 1.20), int(HEIGHT_ / 1.2))
        self.setMinimumSize(int(WIDTH_ / 2), int(HEIGHT_ / 2))
        self.n = 0
### STYLE
        self.style()
### HOME BUTTON
        self.icons()
## button connection    
        self.connection()
## initialisation des Objet
        self.initialisation()
        self.table()
        self.ui.tableWidget.setEnabled(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.show()

    def removeGrid(self) :
        for (C , T) in zip (range(1,(self.nbCircuit*3),3) , self.nb_Circuit) :
            for i in range(0 , T*4,4) :
                w = self.ui.tableWidget.cellWidget(4+i , C)
                self.ui.tableWidget.removeCellWidget(4+i , C )
                i = self.ui.tableWidget.item(4+i , C)
                w.deleteLater()

                #self.ui.tableWidget.update()
    
    def collectData(self) :
        if self.algo ==1 :
            self.DATA={ 
                "immeuble":{
                    'usage':self.ui.usageCombo.currentText(),
                    'hauteur':self.ui.hSpin.value(),
                    'hauteur total':self.ui.hTSpin.value(),
                    'categorie':self.ui.categorieCombo.currentText(),
                    'longueur defini':self.ui.lonDefSpin.value(),
                    'longueur aspiration':self.ui.longAspSpin.value(),
                    'longueur canalisation':self.ui.longCanSpin.value(),
                    'longueur total':self.ui.longTtSpin.value(),
                    'vitesse minimal':self.ui.vMinSpin.value(),
                    'pression reel':self.ui.pressRelSpin.value()
                }
            }
            c_ = 0
            for (C , T) in zip (range(1,(self.nbCircuit*3),3) , self.nb_Circuit) :
                c_+=1
                self.DATA.update({f'circuit {c_}':{}
                })
                t_= 0
                for i in range(0 , T*4,4) :
                    t_ +=1
                    typ = self.ui.tableWidget.cellWidget(3+i,C)
                    long = self.ui.tableWidget.cellWidget(3+i,C+1)
                    self.DATA[f'circuit {c_}'].update({
                        f'troncon {t_}':{
                            "type":typ.currentText(),
                            "longueur":long.value()
                        }
                    })
                    w = self.ui.tableWidget.cellWidget(4+i , C)
                    grid = w.layout() 
                    appareil = 0
                    for pos in range(6) :
                        appareil+=1
                        combo = grid.itemAtPosition(pos,0).widget()
                        spin = grid.itemAtPosition(pos , 1).widget()
                        self.DATA[f'circuit {c_}'][f'troncon {t_}'].update({
                            appareil : [combo.currentText() , spin.value()]
                        })

            #print(json.dumps(self.DATA,indent=4))
            with open ('db/data.json' , 'w') as f:
                f.write(json.dumps(self.DATA , indent=4))
                f.close()
            self.ui.stackedWidget.setCurrentWidget(self.ui.cumputePage)
            self.dataView(data=self.DATA)

        elif self.algo==2 :
            self.DATA={ 
                "immeuble":{
                    'usage':self.ui.usageCombo.currentText(),
                    'altitude':self.ui.hSpin.value(),
                    'hauteur total':self.ui.hTSpin.value(),
                    'categorie':self.ui.categorieCombo.currentText(),
                    'longueur defini':self.ui.lonDefSpin.value(),
                    'longueur aspiration':self.ui.longAspSpin.value(),
                    'longueur canalisation':self.ui.longCanSpin.value(),
                    'longueur total':self.ui.longTtSpin.value(),
                    'vitesse minimal':self.ui.vMinSpin.value(),
                    'pression reel':self.ui.pressRelSpin.value(),
                    'pression residuelle':self.r_press_dspin.value(),
                    'pression au sol':self.s_press_dspin.value()
                }
            }
            c_ = 0
            H = 0
            for (C , T) in zip (range(1,(self.nbCircuit*3),3) , self.nb_Circuit) :
                c_+=1
                self.DATA.update({f'circuit {c_}':{}
                })
                h_spin = self.ui.grid4.itemAtPosition(H+3,3).widget()
                t_= 0 ; H+=1
                print(h_spin)
                print(h_spin.value())
                self.DATA[f'circuit {c_}'].update({"altitude":{}})
                self.DATA[f'circuit {c_}']['altitude'].update({"hauteur":h_spin.value()})
                for i in range(0 , T*4,4) :
                    t_ +=1
                    typ = self.ui.tableWidget.cellWidget(3+i,C)
                    long = self.ui.tableWidget.cellWidget(3+i,C+1)
                    self.DATA[f'circuit {c_}'].update({
                        f'troncon {t_}':{
                            "type":typ.currentText(),
                            "longueur":long.value()
                        }
                    })
                    w = self.ui.tableWidget.cellWidget(4+i , C)
                    grid = w.layout() 
                    appareil = 0
                    for pos in range(6) :
                        appareil+=1
                        combo = grid.itemAtPosition(pos,0).widget()
                        spin = grid.itemAtPosition(pos , 1).widget()
                        self.DATA[f'circuit {c_}'][f'troncon {t_}'].update({
                            appareil : [combo.currentText() , spin.value()]
                        })

            #print(json.dumps(self.DATA,indent=4))
            with open ('db/data.json' , 'w') as f:
                f.write(json.dumps(self.DATA , indent=4))
                f.close()
            self.ui.stackedWidget.setCurrentWidget(self.ui.cumputePage)
            self.dataView(data=self.DATA)
                                
    def circuitItem(self , n ) :
        if isinstance(n , int) == True:
            item = QTableWidgetItem(f"Circuit {n}")
        else:  item = QTableWidgetItem(n)
        item.setFont(QFont('Arial',13,True))
        #item.setBackgroundColor(QColor(127,127,0,30))
        item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.8))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        return item

    def tronconItem(self , n) :
        if isinstance(n , int) == True:
            item = QTableWidgetItem(f"Troncon {n}")
        else:  item = QTableWidgetItem(n)
        item.setFont(QFont('Arial',13,True))
        item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.6))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        return item
    
    def categorieItem(self , n) :
        item = QTableWidgetItem(n)
        item.setFont(QFont('Arial',13,True))
        item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.4))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        return item 

    def item(self , text:str) :
        item = QTableWidgetItem(f"{text}")
        item.setFont(QFont('Arial',13,False))
        item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0.2))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        return item

    def unSelectable(self) :
        for r in range(self.ui.tableWidget.rowCount()) :
            for c in range(self.ui.tableWidget.columnCount()) :
                item = QTableWidgetItem("")
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setBackgroundColor(QColor.fromRgbF(0.2,0.2,0.2,0))
                self.ui.tableWidget.setItem(r,c,item)

    def table(self) :
        if self.calledTable == True : 
            self.removeGrid()
            self.ui.tableWidget.clearContents()
        self.nb_Circuit = [] ; self.spin =[] ; self.calledTable = True
        
        for i in range(self.n) :
            spin = self.ui.grid4.itemAtPosition(i+3, 1).widget()
            self.nb_Circuit.append(spin.value())
        
        if self.ui.tableWidget.isHidden() :
            self.ui.tableWidget.setHidden(False)
        self.ui.tableWidget.setMinimumSize(QSize(0,1000))
        
        self.ui.tableWidget.setColumnCount((self.n*3)+1)
        try : self.ui.tableWidget.setRowCount(4*max(self.nb_Circuit)+1) 
        except Exception : self.ui.tableWidget.setColumnCount(0)
        self.unSelectable()
        

        self.nbCircuit = self.ui.nbCSpin.value() ; n=0

        for (C , T ) in zip (range(1,(self.nbCircuit*3),3) , self.nb_Circuit) :
            self.ui.tableWidget.setColumnWidth(C, 420)

            c=C ; n+=1
            self.ui.tableWidget.setSpan(0,c,1,2)
            self.ui.tableWidget.setSpan(1,c,1,2)

            self.ui.tableWidget.setItem(0,c,self.circuitItem(n))
            self.ui.tableWidget.setItem(2,1,self.item("Type"))
            self.ui.tableWidget.setItem(2,2,self.item("Longueur canalisation"))
            self.ui.tableWidget.setItem(3,0,QTableWidgetItem(""))
            self.ui.tableWidget.setItem(3,2,QTableWidgetItem(""))
            self.ui.tableWidget.setItem(3,3,QTableWidgetItem(""))
            t = 0
            
            for i in range(0,T*4,4) :
                t+=1
                self.ui.tableWidget.setSpan(1+i ,c , 1,2)
                self.ui.tableWidget.setItem(1+i,c, self.tronconItem(t) )   
                spin = QDoubleSpinBox() 
                combo = QComboBox()

                combo.addItems(TRONCON)

                
                self.ui.tableWidget.setItem(2+i,c,self.item("Type"))
                self.ui.tableWidget.setItem(2+i,c+1,self.item("Longueur canalisation"))
                
                self.ui.tableWidget.setCellWidget(3+i,c,combo)
                self.ui.tableWidget.setCellWidget(3+i,c+1,spin)
                self.addGrid(i=i , c = c)
                #self.ui.tableWidget.setItem(4+i,c , QTableWidgetItem(f"data{widget}"))

        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)  

    def addGrid(self , i:int , c:int ) :

        grid = QGridLayout()
        widget = QWidget()
        for j in range(6) : 
            combo  = QComboBox()
            combo.addItems(APPAREIL_LIST)
            spin =  QSpinBox()
            grid.addWidget(combo,j,0,1,1)   
            grid.addWidget(spin,j,1,1,1)
        grid.setContentsMargins(0,50,0,0)
        widget.setContentsMargins(0,0,0,0)
        widget.setLayout(grid)
        #widget.addLayout(grid)
        self.ui.tableWidget.setSpan(4+i,c,1,2)
        self.ui.tableWidget.setRowHeight(4+i,(5)*55 + 50)
        self.ui.tableWidget.setCellWidget(4+i,c,widget) 
        w = self.ui.tableWidget.cellWidget(4,1)

    def changedValue(self) :
        self.removeNbTroncon()
        sleep(0.2)
        self.getNbTroncon()
        #self.ui.tableWidget.setHidden(True)    

    def getNbTroncon(self) :
        self.n = self.ui.nbCSpin.value()
        for i in range(self.n) :
            lab = QLabel(self.ui.scrollAreaWidgetContents)
            lab.setText(f"Troncon du circuit {i+1}")
            self.ui.grid4.addWidget(lab,3+i,0,1,1)

            self.spinTronconNb = QSpinBox(self.ui.scrollAreaWidgetContents)
            self.ui.grid4.addWidget(self.spinTronconNb,3+i,1,1,1)
            self.spinTronconNb.valueChanged.connect(lambda: self.table())

            lab = QLabel(self.ui.scrollAreaWidgetContents)
            lab.setText("Hauteur du circuit")
            self.ui.grid4.addWidget(lab,3+i,2,1,1)

            spin = QDoubleSpinBox()
            spin.setMinimum(3)
            self.ui.grid4.addWidget(spin,3+i,3,1,1)

            if i == self.n - 1 :
                button = QPushButton()
                button.setText("Commencer")
                button.clicked.connect(lambda : self.commencer())
                self.ui.grid4.addWidget(button ,4+i,0,1,1)

                button = QPushButton()
                button.setText("Reprendre")
                button.clicked.connect(lambda : self.reprendre())
                self.ui.grid4.addWidget(button , 4+i,1,1,1)

    def commencer(self) :
        self.ui.tableWidget.setEnabled(True)
        self.ui.nbCSpin.setEnabled(False)
        for i in range(self.ui.nbCSpin.value()) :
            self.ui.grid4.itemAtPosition(3+i,1).widget().setEnabled(False)
    
    def reprendre(self) :
        self.ui.tableWidget.setEnabled(False)
        self.ui.nbCSpin.setEnabled(True)
        for i in range(self.ui.nbCSpin.value()) :
            self.ui.grid4.itemAtPosition(3+i,1).widget().setEnabled(True)
            
    def removeNbTroncon(self) :
        for i in range(self.n ):
            lab = self.ui.grid4.itemAtPosition(3+i,0).widget()
            self.ui.grid4.removeWidget(lab)
            lab.deleteLater()

            spin = self.ui.grid4.itemAtPosition(3+i,1).widget()
            self.ui.grid4.removeWidget(spin)
            spin.deleteLater()

            lab = self.ui.grid4.itemAtPosition(3+i,2).widget()
            self.ui.grid4.removeWidget(lab)
            lab.deleteLater()

            spin = self.ui.grid4.itemAtPosition(3+i,3).widget()
            self.ui.grid4.removeWidget(spin)
            spin.deleteLater()


            if i== self.n -1:
                button = self.ui.grid4.itemAtPosition(4+i,0).widget()
                self.ui.grid4.removeWidget(button)
                button.deleteLater()
            
                button = self.ui.grid4.itemAtPosition(4+i,1).widget()
                self.ui.grid4.removeWidget(button)
                button.deleteLater()
            
    def connection(self) :
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        self.ui.paraBtn.clicked.connect(lambda: self.ui_parapluie())
        self.ui.surpBtn.clicked.connect(lambda: self.ui_surpression() )    
        self.ui.backToPara.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paraPage))
        self.ui.getDataBtn.clicked.connect(lambda : self.collectData())
        self.ui.nbCSpin.valueChanged.connect(lambda :self.changedValue())
        self.ui.calculBtn.clicked.connect(lambda: self.resultView() )

    def initialisation(self) :
        self.calledTable = False
        self.ui.categorieCombo.addItems(CATEGORIE)

        self.ui.getDataBtn.setText("Recapitulatif")
        self.ui.backToPara.setText("Retour")
        self.ui.calculBtn.setText("Effectuez les operations")

        self.ui.label1Para.setText("Etape 1: Caracteristique de l'immeuble")
        self.ui.label2Para.setText("Etape 2: Information sur la tuyauterie")
        self.ui.label3Para.setText("Etape 3: Informations sur l'eau")
        self.ui.label4Para.setText("Etape 4: Inventaire des appareils")
        self.ui.usageLab.setText("Usage")
        self.ui.hLab.setText("Hauteur")
        self.ui.hTLab.setText("Hauteur total")

        self.ui.label1Para.setAlignment(Qt.AlignCenter)
        self.ui.label2Para.setAlignment(Qt.AlignCenter)
        self.ui.label3Para.setAlignment(Qt.AlignCenter)
        self.ui.label4Para.setAlignment(Qt.AlignCenter)
        

        self.items = USAGE_LIST
        self.ui.usageCombo.addItems(self.items)

        self.ui.categorieLab.setText("Categorie")
        self.ui.lonDefLab.setText("Longueur definir")
        self.ui.longAspLab.setText("Longueur d'aspiration ")
        self.ui.longCanLab.setText("Longueur de canalisation")
        self.ui.longTtLab.setText("Longueur total de conduite")

        self.ui.vMinLab.setText("Vitesse minimal")
        self.ui.pressRelLab.setText("Pression réèl")
        self.ui.nbCLab.setText("Nombre total de circuit")

        return "Done"
        
    def style(self) :
## central backgroud
        self.ui.centralwidget.setStyleSheet("""#centralwidget{background-image:url("""+img_+""");background-repeat:reapeat;background-position: left top center;border:0}""" )
        self.ui.stackedWidget.setStyleSheet("background:transparent")
        self.ui.slidWidget.setStyleSheet("background:transparent")
        self.ui.stackedWidget.setStyleSheet("""
        QPushButton{ background:transparent } 
        QGridLayout{ background:transparent }
        QLabel{background:transparent}
        QWidget{background:transparent}
        """)
## slide button
        slidBtn = [self.ui.menuBtn ,  self.ui.homeBtn , self.ui.dataBtn , self.ui.infosBtn]
        path_ = ['menu.svg','home.svg','database-settings.svg','information-outline.svg']
        [(btn.setStyleSheet("""background:transparent,:hover{
        background: rgba(195,195,195,1);}""") ,
        btn.setIcon(QtGui.QIcon("icons/"+path)),
        btn.setIconSize(QSize(40,40))) for (btn,path) in zip(slidBtn , path_) ]
## scroll AREA
        self.ui.scrollArea.setStyleSheet(scrollStyle)

    def icons(self) :
        start = QSize(240,240)
        end =  QSize(370,370)
        duration=[2500,2500]
        loop = 100
        self.ui.paraBtn.setIcon(QtGui.QIcon("icons/parachute-outline.svg"))
        self.ui.surpBtn.setIcon(QtGui.QIcon("icons/camera-timer.svg"))

        #self.ui.paraBtn.setStyleSheet("background:transparent;")
        #self.ui.surpBtn.setStyleSheet("background:transparent;")
        self.ui.paraBtn.setStyleSheet(":hover{background: rgba(195,195,195,0.35);}")
        self.ui.surpBtn.setStyleSheet(":hover{background: rgba(195,195,195,0.35);}")
        

        self.animPara0 = QPropertyAnimation(self.ui.paraBtn,b"iconSize")
        self.animPara0.setEndValue(start)
        self.animPara0.setDuration(duration[0])
        self.animePara1 = QPropertyAnimation(self.ui.paraBtn , b"iconSize")
        self.animePara1.setStartValue(start)
        self.animePara1.setEndValue(end)
        self.animePara1.setDuration(duration[1])
        self.animePara1.setLoopCount(loop)
        #self.animParaGroup = QParallelAnimationGroup()
        self.animParaGroup =  QSequentialAnimationGroup()
        self.animParaGroup.addAnimation(self.animPara0)
        self.animParaGroup.addAnimation(self.animePara1)


        self.animSurp0 = QPropertyAnimation(self.ui.surpBtn,b"iconSize")
        self.animSurp0.setEndValue(start)
        self.animSurp0.setDuration(duration[0])
        self.animSurp1 = QPropertyAnimation(self.ui.surpBtn , b"iconSize")
        self.animSurp1.setStartValue(start)
        self.animSurp1.setEndValue(end)
        self.animSurp1.setDuration(duration[1])
        self.animSurp1.setLoopCount(loop)
        #self.animSurpGroup = QParallelAnimationGroup()
        self.animSurpGroup =  QSequentialAnimationGroup()
        self.animSurpGroup.addAnimation(self.animSurp0)
        self.animSurpGroup.addAnimation(self.animSurp1)

        self.animParaGroup.start()
        self.animSurpGroup.start() 

    def dataView(self , data:dict) :
        infos = {} ; c = 0 ; t = 0
        for k in list(data.keys())[1:] :
            c += 1 ; infos.update({c:{}})
            for k_ in data[k].keys() :
                t += 1 ; infos[c].update({t:[]})
                for k__ in data[k][k_] :
                    infos[c][t].append(k__)
    
        print(infos)
        self.ui.recapTable.setRowCount( (c+t)*3+(10) )
        self.ui.recapTable.setColumnCount(10)
        
        for (key , c) in zip (data['immeuble'].keys(),range(10)) :
            self.ui.recapTable.setItem(1,c,self.tronconItem( key.capitalize() ))
            self.ui.recapTable.setItem(2,c,self.item( data['immeuble'][key]))

        self.ui.recapTable.setSpan(0,0,1,10)
        self.ui.recapTable.setItem(0,0,self.circuitItem("Informations sur l'immeuble"))    
        self.ui.recapTable.setMinimumSize(QSize(0,1000))

        ROW = 3
        for KEY in list(data.keys())[1:] :
            self.ui.recapTable.setSpan(ROW,0,1,10)
            self.ui.recapTable.setItem(ROW,0,
                        self.circuitItem(str(KEY).capitalize()))
            ROW+=1 
            for Key in data[KEY].keys() :
                self.ui.recapTable.setSpan(ROW,0,1,10)
                self.ui.recapTable.setItem(ROW,0,self.item(""))
                ROW+=1
                self.ui.recapTable.setSpan(ROW,0,1,10)
                self.ui.recapTable.setItem(ROW, 0 , 
                        self.tronconItem(str(Key).capitalize()))
                ROW+=1
                for key in data[KEY][Key].keys() :
                    self.ui.recapTable.setSpan(ROW,0,1,10)
                    if str(key) == 'type' :
                        self.ui.recapTable.setItem(ROW,0,
                            self.categorieItem(str(key)))
                        ROW+=1
                        self.ui.recapTable.setSpan(ROW,0,1,5)
                        self.ui.recapTable.setItem(ROW,0,
                            self.item( data[KEY][Key][key] ))
                        ROW+=1
                    else :
                        self.ui.recapTable.setItem(ROW,0,
                            self.categorieItem("Categorie"+str(key)))
                        ROW+=1
                        self.ui.recapTable.setSpan(ROW,0,1,5)
                        self.ui.recapTable.setItem(ROW,0,
                            self.item( data[KEY][Key][key] ))    
                        ROW+=1                    

    def resultView(self) :
        self.ui.resultTable.setMinimumSize(QSize(0,1000))
        pass
        
    def ui_parapluie(self) :
        self.algo = 1
        self.ui.stackedWidget.setCurrentWidget(self.ui.paraPage)

    def ui_surpression(self) :
        self.algo = 2

        self.ui.hLab.setText("Altitude")
        self.r_press_lab = QLabel()
        self.r_press_lab.setText("Pression residuelle")
        self.r_press_dspin = QDoubleSpinBox()
        self.ui.grid3.addWidget(self.r_press_lab,2,0,1,1)
        self.ui.grid3.addWidget(self.r_press_dspin ,2,1,1,1)
        
        self.s_press_lab = QLabel()
        self.s_press_lab.setText("Pression au sol")
        self.s_press_dspin = QDoubleSpinBox()
        self.s_press_dspin.setMinimum(2.0)
        self.ui.grid3.addWidget(self.s_press_lab,3,0,1,1)
        self.ui.grid3.addWidget(self.s_press_dspin,3,1,1,1)

        self.ui.paraLab.setText("Systeme de distributione en surpression")

        self.ui.stackedWidget.setCurrentWidget(self.ui.paraPage)