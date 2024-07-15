import typing
from PyQt5.QtCore import QObject
from UI.lib import *
from UI.maStrategy import maStrategy
from UI.Suport import Support

class SelectData(QWidget) :
    def __init__(self , parent: QStackedWidget=None):
        super().__init__(parent)
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)

        self.label = BodyLabel(("Cliquer pour choisir une base de donnees"))
        self.btn = PushButton('Cliquer', self, FIF.DOWNLOAD)  
        self.nextBtn = PushButton("Suivant" , self , FIF.PAGE_RIGHT )
              
        self.vBox.addWidget(self.label ,1, HCENTER|CENTER )
        self.vBox.addWidget(self.btn, 0, HCENTER|TOP )
        self.vBox.setSpacing(20)
        self.vBox.addWidget(self.nextBtn , 0 , RIGHT|BOTTOM)

        self.stateTooltip = None
        self.filePath=None
        
        self.state= StateToolTip('','Fichier .CSV', self)
        self.state.move(510, 30)
        self.nextBtn.setEnabled(False)
        
    def operation(self) :
        self.t1 = QThread()


    def fileDialog(self) :
        self.nextBtn.setEnabled(False)
        self.state.setHidden(True)
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;XLSX (*.xlsx)")
        
        if self.stateTooltip==None:    
            self.stateTooltip = StateToolTip('','Fichier .CSV', self)
            self.stateTooltip.move(510, 30)
            self.stateTooltip.show()
        self.onButtonClicked()
        

    def onButtonClicked(self):
        if self.stateTooltip : 
            if self.filePath:
                self.stateTooltip.setTitle("✔ ✔ ✔")
                self.stateTooltip.setContent(f'{ Path(self.filePath).name }')
                self.stateTooltip.setState(True)
                self.nextBtn.setEnabled(True)
                self.stateTooltip = None
                
            else :
                self.stateTooltip.setTitle("❌ ❌ ❌")            

    def nextPage(self , next : QWidget , parent:QStackedWidget) :
        if self.filePath :
            parent.setCurrentWidget(next)


class collectInformation(SmoothScrollArea) :
    def __init__(self  , parent: QStackedWidget=None) :
        super().__init__(parent)       
        
    def initGrid(self , file) :
        self.Widget = QWidget(self)
        self.grid = QGridLayout(self.Widget)
        
        
        self.lab = SubtitleLabel(("Profil d'investissement."))
        self.lab.setContentsMargins(0,15,0,15)
        self.grid.addWidget(self.lab ,0,0,1,2,CENTER|CENTER)
        
        
        self.lab = StrongBodyLabel(("Objectif d'investissement"))
        self.objectifCombo = ComboBox(self)
        self.objectifCombo.addItems([
        "Croissance de capital" , "Protection du patrimoine","Speculer sur les marches","Revenu regulier"])
        self.grid.addWidget(self.lab,1,0,1,2,LEFT|VCENTER)
        self.grid.addWidget(self.objectifCombo,2,0,1,1)
        
        
        self.lab = StrongBodyLabel(("Horizon temporel"))
        self.horizonCombo = ComboBox(self)
        self.horizonCombo.addItems([
        "Court terme" , "Moyen terme","Long terme","Tres court terme"])
        self.moisCombo = ComboBox(self) ; self.moisCombo.addItems(["1. mois(30 jous) " , "2. mois(60 jours)" , "3. mois(90 jours)","4. mois(120 jours) ", "Mois de 1 mois"])
        self.grid.addWidget(self.lab, 3 , 0,1,2,LEFT|VCENTER)
        self.grid.addWidget(self.horizonCombo,4,0,1,1)
        self.grid.addWidget(self.moisCombo,4,1,1,1,LEFT|TOP)
        
        
        self.lab = StrongBodyLabel(("Tolerance au Risque"))
        self.toleranceCombo = ComboBox(self)
        self.toleranceCombo.addItems([
        "Prudent" , "Moderer" , "Energetique" ])
        self.grid.addWidget(self.lab,5,0,1,2,LEFT|VCENTER)    
        self.grid.addWidget(self.toleranceCombo,6,0,1,1)    


        self.lab = SubtitleLabel(("Configuration des parametres."))
        self.lab.setContentsMargins(0,15,0,15)
        self.grid.addWidget(self.lab,7,0,1,2,CENTER|CENTER)
        
        
        self.lab = StrongBodyLabel(("Informations sur la base de donnees"))
        self.grid.addWidget(self.lab, )
        
        try :
            if Path(file).exists()==True :
                df = read_csv(file)
                self.column = df.columns
            else :
                df = "None"
                self.column = " None "
        except Exception : self.column = " None " ; df = "None"
        self.grid.addWidget(self.lab , 8,0,1,2)
        
        
        self.lab1 = BodyLabel(("Date : "))    
        self.lab2 = BodyLabel(("Prix de cloture : "))
        self.combo1 = ComboBox(self)
        self.combo1.addItems( list(self.column) )
        if "Date" in list(self.column) : self.combo1.setCurrentText("Date")
        self.combo2 = ComboBox(self)
        self.combo2.addItems( list(self.column) )
        if "Close" in list(self.column) : self.combo2.setCurrentText("Close")

        self.grid.addWidget(self.lab1,9,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.lab2,10,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.combo1,9,0,1,1,HCENTER|CENTER)
        self.grid.addWidget(self.combo2,10,0,1,1,HCENTER|CENTER)
        
        
        self.lab = StrongBodyLabel(("Simulation "))
        self.grid.addWidget(self.lab , 11,0,1,2,LEFT|CENTER)
        
        
        self.lab = CaptionLabel(("(utiliser les intervalles de dates ou les intervalles de nombres pour choisir une portion de donnees)"))
        self.grid.addWidget(self.lab , 12,0,1,1,LEFT|TOP)
        
        
        self.lab = BodyLabel(("Intervalle :"))
        self.date1 = DateEdit(self)
        self.date2 = DateEdit(self)
        self.grid.addWidget(self.lab,13,0,1,2,LEFT|CENTER)
        self.grid.addWidget(self.date1,13,0,1,1,RIGHT|CENTER)
        self.grid.addWidget(self.date2,13,1,1,1,LEFT|CENTER)
        
        
        self.lab = BodyLabel(("Intervalle : "))
        self.intervalle1 = SpinBox(self)
        self.intervalle2 = SpinBox(self) 
        self.intervalle1.setMaximum(len(df))
        self.intervalle1.setValue(len(df)-60)
        self.intervalle2.setMaximum(len(df))
        self.intervalle2.setValue(len(df))
        self.grid.addWidget(self.lab,14,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.intervalle1,14,0,1,1,RIGHT|CENTER)
        self.grid.addWidget(self.intervalle2,14,1,1,1,LEFT|CENTER)        

        
        self.lab = BodyLabel(("parametres rapide : "))
        self.rapide1 = SpinBox(self)
        self.rapide2 = SpinBox(self)
        self.rapide1.setMinimum(5)
        self.rapide2.setMinimum(10)
        self.grid.addWidget(self.lab,15,0,1,1,LEFT|CENTER)
        self.lab = CaptionLabel(("(intervalle de pariode a tester\npour la moyenne mobile rapide)"))
        self.grid.addWidget(self.lab,15,0,1,1,CENTER|CENTER)
        self.grid.addWidget(self.rapide1,15,0,1,1,RIGHT|CENTER)
        self.grid.addWidget(self.rapide2,15,1,1,1,LEFT|CENTER)


        self.lab = BodyLabel(("Parametres lente : "))
        self.lente1 = SpinBox(self)
        self.lente2 = SpinBox(self)
        self.lente1.setMinimum(5)
        self.lente2.setMinimum(10)
        self.grid.addWidget(self.lab,16,0,1,1,LEFT|CENTER)
        self.lab = CaptionLabel(("(intervalle de pariode a tester\npour la moyenne mobile lente)"))
        self.grid.addWidget(self.lab,16,0,1,1,CENTER|CENTER)
        self.grid.addWidget(self.lente1,16,0,1,1,RIGHT|CENTER)
        self.grid.addWidget(self.lente2,16,1,1,1,LEFT|CENTER)
              

        self.lab = BodyLabel(("Difference minimum entre les periodes :"))
        self.diffSpin = SpinBox(self)
        self.diffSpin.setMinimum(2)
        self.grid.addWidget(self.lab,17,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.diffSpin,17,0,1,1,RIGHT|CENTER)
        
        
        self.lab = BodyLabel(("Minimun de benefice souhaiter (en %):"))
        self.minBenefice = SpinBox(self)
        self.minBenefice.setMinimum(20)
        self.grid.addWidget(self.lab,18,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.minBenefice,18,0,1,1,RIGHT|CENTER)
        
        
        self.lab = BodyLabel(("Minimun de transaction positive (en %):"))
        self.minTransaction = SpinBox(self)
        self.minTransaction.setMinimum(20)
        self.grid.addWidget(self.lab,19,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.minTransaction,19,0,1,1,RIGHT|CENTER)
        
        
        spacer = QWidget()
        spacer.setMinimumHeight(50)
        n = self.grid.rowCount()
        self.grid.addWidget(spacer,n+1,0)
                  
        
        self.navigationFrame=QFrame(self)
        hBox=QHBoxLayout(self.navigationFrame)
        self.navigationFrame.setLayout(hBox)
        self.backBtn = PushButton("Back" , self , FIF.PAGE_LEFT)
        self.nextBtn = PushButton("Next ", self , FIF.PAGE_RIGHT)
        hBox.addWidget(self.backBtn,0,LEFT|CENTER)
        hBox.addWidget(self.nextBtn,0,RIGHT|CENTER) 
        self.backBtn.setToolTip("""⬅""")
        self.nextBtn.setToolTip("""➡ """)
        self.navigationFrame.setContentsMargins(0,0,0,0)
        hBox.setContentsMargins(0,0,0,0)
        
        
        self.grid.setSpacing(10)
        self.Widget.setLayout(self.grid)
        self.setWidget(self.Widget)
        self.setWidgetResizable(True)
        self.Widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)    
        
    def nextPage(self , next : [QWidget] , parent:QStackedWidget) :
        parent.setCurrentWidget(next)
        
    def previewPage(self , preview : [QWidget] , parent:QStackedWidget) :
        parent.setCurrentWidget(preview)

class maResults(SmoothScrollArea) :
    def __init__(self  , parent: QStackedWidget=None) :
        super().__init__(parent)
        self.Widget = QWidget(self)
        self.vBox = QVBoxLayout(self.Widget)
        self.vBox.setContentsMargins(10,10,40,0)
        self.Widget.setLayout(self.vBox)
        
        ### 
        self.startBtn = PushButton("commencer",self.Widget , FIF.PLAY)
        self.vBox.addWidget(self.startBtn,0,LEFT|CENTER)        
        
        ##
        self.lab_= SubtitleLabel("Resultats des simulations")
        self.vBox.addWidget(self.lab_,0,HCENTER|CENTER)
        self.lab_.setContentsMargins(0,25,0,0)
        self.lab_.setHidden(True)
        
        #Text Edit :
        self.frame = QFrame(self.Widget)
        self.parametreProgessTextEdit = TextEdit(self.Widget)
        self.resultProgressTextEdit = TextEdit(self.Widget)
        self.hBox = QHBoxLayout()
        self.frame.setLayout(self.hBox)
        self.hBox.addWidget(self.parametreProgessTextEdit)
        self.hBox.addWidget(self.resultProgressTextEdit)
        self.frame.setMinimumHeight(600)
        
        self.vBox.addWidget(self.frame)

        # Resistance Support image view frame and label
        self.lab = SubtitleLabel("Ligne de Support de de Resistance")
        self.vBox.addWidget(self.lab,0,HCENTER|CENTER)
        self.lab.setContentsMargins(0,25,0,0)
        self.imageScrollArea = SmoothScrollArea(self.Widget)
        self.frame = QFrame(self.imageScrollArea)
        self.labViewResistance = PixmapLabel(self.frame)     
        self.frame.vbox = QVBoxLayout(self.frame)
        self.frame.vbox.addWidget(self.labViewResistance)
        self.frame.setLayout(self.frame.vbox)
        self.imageScrollArea.setWidget(self.frame)
        self.imageScrollArea.setWidgetResizable(True)
        self.frame.setMinimumHeight(600)
        self.imageScrollArea.setMinimumHeight(600)
        
        self.vBox.addWidget(self.imageScrollArea)
        
        # image view frame and label
        self.lab = SubtitleLabel("Tendance des prix de cloture")
        self.vBox.addWidget(self.lab,0,HCENTER|CENTER)
        self.lab.setContentsMargins(0,20,0,0)
        self.imageScrollArea = SmoothScrollArea(self.Widget)
        self.frame = QFrame(self.imageScrollArea)
        self.labView = PixmapLabel(self.frame)     
        self.frame.vbox = QVBoxLayout(self.frame)
        self.frame.vbox.addWidget(self.labView)
        self.frame.setLayout(self.frame.vbox)
        self.imageScrollArea.setWidget(self.frame)
        self.imageScrollArea.setWidgetResizable(True)
        self.frame.setMinimumHeight(600)
        self.imageScrollArea.setMinimumHeight(600)
        
        self.vBox.addWidget(self.imageScrollArea)
        
        ## Navigation Button 
        self.navigationFrame = QFrame(self.Widget)
        self.backBtn = PushButton("Back " , self.navigationFrame , FIF.PAGE_LEFT)
        self.nextBtn = PushButton("Next" , self.navigationFrame , FIF.PAGE_RIGHT)
        hBox = QHBoxLayout(self.navigationFrame)
        self.navigationFrame.setLayout(hBox)
        hBox.addWidget(self.backBtn,0,LEFT|BOTTOM)
        hBox.addWidget(self.nextBtn, 0 , RIGHT|BOTTOM)
        self.navigationFrame.setContentsMargins(0,0,0,0)
        hBox.setContentsMargins(0,0,0,0)
        
        self.vBox.addWidget(self.navigationFrame)
        self.long_process_thread = None
        
        ## Area Widget
        self.setWidget(self.Widget)
        self.setContentsMargins(20,20,20,0)
        self.setWidgetResizable(True)            
    
    def updateLabel(self,message) :
        pixmap = QPixmap(r"resource/MA_resistance.png")
        self.labViewResistance.setPixmap(pixmap)
        pixmap = QPixmap(message)
        self.labView.setPixmap(pixmap)
        

    def parametreProgress(self , parameter):
        if self.long_process_thread is None or not self.long_process_thread.isRunning():
            #self.parametreProgessTextEdit.setEnabled(False)
            # You can set your desired parameter here
            self.long_process_thread = LongProcessThread(parameter)
            self.long_process_thread.update_signal.connect( self.update_text_edit)
            self.long_process_thread.start()

    def update_text_edit(self, message):
        self.parametreProgessTextEdit.append(
            message['message1']  )
        if message['message2'] :
            self.resultProgressTextEdit.append(
            message['message2'])
        if message['last'] ==True :
            self.startBtn.setEnabled(True) 






class maDataBase(SmoothScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        ## Frame head
        self.frame = QFrame(self)
        hBox = QHBoxLayout(self.frame)
        self.frame.setLayout(hBox)
        self.LineEdit = LineEdit(self.frame)
        self.startBtn = PushButton(" ",self.frame,FIF.PLAY)
        self.lineEditBtn = LineEditButton(FIF.SEARCH,self.frame)
        hBox.addWidget(self.LineEdit)
        hBox.addWidget(self.lineEditBtn)
        hBox.addWidget(self.startBtn)
        
        self.Widget = QWidget(self)
        self.vBox = QVBoxLayout(self.Widget)
        self.Widget.setLayout(self.vBox)
        # Table Widget
        self.tableWidget = TableWidget(self.Widget)
        self.vBox.addWidget(self.tableWidget)
        ## Bottom navigation buttom
        self.backBtn  = PushButton("Back",self,FIF.PAGE_LEFT)
        self.setWidget(self.Widget)
        self.setWidgetResizable(True)
        self.vBox.setContentsMargins(0,10,30,0)

        self.process = None
        self.startBtn.clicked.connect(self.LongProcess)
        
    
    def updateTable(self,message) :
        """i = message['i']
        data = message['data']
        self.tableWidget.insertRow(i)
        for j in range(len(data)) :
            self.tableWidget.setItem(i,j,QTableWidgetItem(str(data[j])))
            sleep(400)"""
        self.tableWidget.update()

    
    def LongProcess(self) :
        if self.process is None or self.process.isFinished()==True:
            self.process = tableWidgetThread(table=self.tableWidget)
            self.process.update_signal.connect(self.updateTable)
            self.process.start()

        
class createImageThread(QThread):
    update_signal = pyqtSignal(str) 
    def __init__(self, df:str , col:str,debut:int,fin:int,
            rapide:int,lente:int) :
        super().__init__()
        self.df_path = df 
        self.col = col 
        self.rapide = rapide
        self.lente = lente
        self.debut =  debut
        self.fin = fin
    
    def run(self):
        filename = r"resource/MA_Preview.png"
        plt.figure(figsize=(16,10),dpi=200)
        self.df = read_csv(self.df_path, index_col=self.col)
        
        self.df = self.df[self.debut : self.fin]
        plt.plot(self.df["Close"].index, self.df["Close"].values , label="close",linewidth=1)
        plt.plot(self.df["Close"].index, self.df["Close"].rolling(self.rapide).mean() , label="fast",linewidth=1)
        plt.plot(self.df["Close"].index, self.df["Close"].rolling(self.lente).mean() , label="low",linewidth=1)
        

        position = []
        for i in range(0 , len(self.df) , int(len(self.df)/8)) : position.append(i)
        labels = [self.df.iloc[int(i)].name for i in position]
        plt.xticks(position,labels,rotation=45)

        plt.title(f"{Path(self.df_path).stem} ({self.debut} - {self.fin})")
        plt.legend()
        plt.subplots_adjust(top=0.2, bottom=0.1)
        plt.set_cmap("tab20c")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        im = Image.open(filename)
        im1 = im.resize((1200,600))
        im1.save(filename)
        im.close() ; im1.close()
        
        resistance = Support(df=self.df,col="Close")
        resistance.support_resistance()
        im = Image.open(r"resource\MA_resistance.png")
        im1 = im.resize((1200,600))
        im1.save(r"resource\MA_resistance.png")
        
        self.update_signal.emit(filename)
        

class LongProcessThread(QThread):
    update_signal = pyqtSignal(dict)

    def __init__(self, parameter):
        super().__init__()
        self.infos = parameter
        self.data = read_csv(self.infos["name"] , index_col=self.infos['indix'])
        self.data = self.data[self.infos["debut"] : self.infos["fin"]]
        self.r1 = self.infos['rapide'][0] ; self.r2=self.infos['rapide'][1]
        if self.r1 > self.r2 : self.r1,self.r2 = self.r2,self.r1
        
        self.l1 = self.infos["lente"][0] ; self.l2 = self.infos["lente"][1] 
        if self.l1 > self.l2 : self.l1,self.l2 = self.l2 , self.l1
        
    def run(self):
        self.msleep(4000)
        rapide,lente,positive,negative,total,benefice=[],[],[],[],[],[]
        stick = []
        for i in range( self.r1 , self.r2+1 ) :
            for j in range(self.l1 , self.l2):
                if j>i+2 : 
                    self.data_ = self.data[[self.infos['close']]]
                    
                    self.strategy = maStrategy(
                    df=self.data_,r=i,l=j,col=self.infos['close'] )
                    self.resultat = self.strategy.strategy()
                    
                    if self.resultat<0 : self.emotion = "❌ ❌"
                    elif self.resultat == 0 : self.emotion = "🕳🕳"
                    elif self.resultat >0 and self.resultat <20 : self.emotion = "❗ ❗"
                    else : self.emotion = "✅✅✅ "
                    
                    message1 = f"Moyenne Mobile Rapide : {i} \nMoyenne Mobile Lente : {j} \n"
                    message1+=f"Transaction Positive {self.strategy.positive}\n"
                    message1+="Transaction Negative {self.strategy.negative}\n"
                    message1+=f"Pourcentage de benefice realiser : {self.resultat} {self.emotion}\n"
                    
                    if self.infos["min_benef"] <= self.resultat and  ( 
                        (j-i) <= self.infos["min_diff"]) and self.infos["min_transaction"] <= (self.strategy.positive/self.strategy.total)*100 :
                        message2 = message1
                    else : 
                        message2 = None
                    
                    self.update_signal.emit({
                        "last":False,
                        "message1":message1,
                        "message2":message2
                    })
                    
                    rapide.append(i)
                    lente.append(j)
                    positive.append(f"{round((self.strategy.positive/self.strategy.total)*100,2)} %")
                    negative.append(f"{round((self.strategy.negative/self.strategy.total)*100,2)} %")
                    total.append(self.strategy.total)
                    benefice.append(f"{self.strategy.pourcentage_revenu} %")
                    if self.strategy.pourcentage_revenu <= 10 : stick.append("❗")
                    else:stick.append("✅")
                    
                    del(self.strategy)
                    self.msleep(800)
        DATA = {
            "📎":stick,
            "Rapide(period)":rapide ,
            "Lente":lente,
            "Positive(transaction)":positive,
            "Negative":negative,
            "Total":total,
            "Benefice":benefice
        }
        DataFrame(DATA).to_csv(r"db/MA_DATABASE.csv")
        self.update_signal.emit({
            "message1":"",
            "message2":"",
            "last":True })

class tableWidgetThread(QThread) :
    update_signal = pyqtSignal(dict)
    
    def __init__(self , table:TableWidget) -> None:
        super().__init__()
        self.df = read_csv("db/MA_DATABASE.csv",index_col=0)
        self.table = table
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(list(self.df.columns))
        
    def run(self) :
        
        t=self.table.rowCount()
        for k in range(t) :
            self.table.removeRow(0)
            self.update_signal.emit({3:3})
            self.msleep(5)
        
        taille = len(self.df)
        colTaiile = len(self.df.iloc[1])
        for i in range(len(self.df )) :
            self.table.insertRow(i)    
            self.table.selectRow(i)        
            for j in range(len(self.df.iloc[i])) :
                self.table.setItem(i,j,QTableWidgetItem(str(self.df.iloc[i][j])))
                self.update_signal.emit({1:3})
                self.msleep(1)
        self.table.selectRow(0)
        #self.update_signal.emit({"i":i,"len":taille,"data":self.df.iloc[i]})
        