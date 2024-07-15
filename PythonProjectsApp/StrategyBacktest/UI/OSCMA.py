from .lib import *
from qfluentwidgets import BodyLabel
import qtawesome  as qta
from UI.OS_Strategie import OS_MACD


class ScrollAr(SmoothScrollArea) :
    def __init__(self, parent=None):
        super().__init__(parent)


class getDataInterface(QWidget) :
    def __init__(self , parent=None) :
        super().__init__(parent)
        
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)
        
        self.label = BodyLabel("Cliquer pour choisir une base de donnees")
        self.btn = PushButton("Cliquer" , self,qta.icon("fa5s.file-download"))
        self.nextBtn = PushButton("Suivant" , self , qta.icon("ei.arrow-right"))

        self.vBox.addWidget(self.label,1,HCENTER|CENTER)
        self.vBox.addWidget(self.btn,0,HCENTER|TOP)
        self.vBox.setSpacing(20)
        self.vBox.addWidget(self.nextBtn, 0 , RIGHT|BOTTOM)

        self.stateTooltip = None
        self.filePath=None
        
        self.state= StateToolTip('','Fichier .CSV', self)
        self.state.move(800, 30)
        self.nextBtn.setEnabled(False)

        self.btn.clicked.connect(self.fileDialog)

    def operation(self) :
        self.t1 = QThread()

    def fileDialog(self) :
        self.nextBtn.setEnabled(False)
        self.state.setHidden(True)
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;XLSX (*.xlsx)")
        
        if self.stateTooltip==None:    
            self.stateTooltip = StateToolTip('','Fichier .CSV', self)
            self.stateTooltip.move(800, 30)
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


class getStrategiInfosInterface(QWidget) :
    def __init__(self , parent=None) :
        super().__init__(parent)

        self.Widget = QWidget(self)
        self.scrollArea = SmoothScrollArea(self)

## Object de collect des information
        self.grid = QGridLayout(self.Widget)
        self.Widget.setLayout(self.grid)
        
        self.lab = SubtitleLabel("Information sur la base de donnees")
        self.grid.addWidget(self.lab,0,0,1,2,CENTER|CENTER)
        
        self.lab1 = BodyLabel(("Date : "))
        self.lab2 = BodyLabel(("Prix de clôture"))
        self.lab3 = BodyLabel(("PLus Haut"))
        self.lab4 = BodyLabel(("PLus Bas"))
        self.combo1 = ComboBox(self.Widget)
        self.combo2 = ComboBox(self.Widget)
        self.combo3 = ComboBox(self.Widget)
        self.combo4 = ComboBox(self.Widget)

        self.grid.setSpacing(0)
        self.grid.addWidget(self.lab1,1,0,1,1)
        self.grid.addWidget(self.combo1,2,0,1,1)
        self.grid.addWidget(self.lab2,  3,0,1,1)
        self.grid.addWidget(self.combo2,4,0,1,1)
        self.grid.addWidget(self.lab3,  5,0,1,1)
        self.grid.addWidget(self.combo3,6,0,1,1)
        self.grid.addWidget(self.lab4,7,0,1,1)
        self.grid.addWidget(self.combo4,8,0,1,1)

        self.lab = SubtitleLabel("Configuration des parametres ")
        self.grid.addWidget(self.lab,9,0,1,2,CENTER|CENTER)
        
        self.lab1 = BodyLabel(("Periodes moyennes mobile rapide (MACD)"))
        self.spinRapide1 = SpinBox(self.Widget) ; self.spinRapide1.setMinimumWidth(150)
        self.spinRapide2 = SpinBox(self.Widget) ; self.spinRapide2.setMinimumWidth(150)
        self.lab2 = BodyLabel(("Periodes moyennes mobile lente (MACD)"))
        self.spinLente1 = SpinBox(self.Widget) ; self.spinLente1.setMinimumWidth(150)
        self.spinLente2 = SpinBox(self.Widget)  ; self.spinLente2.setMinimumWidth(150)
        
        self.grid.addWidget(self.lab1,10,0,1,1)
        self.grid.addWidget(self.spinRapide1,11,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.spinRapide2,11,0,1,1,RIGHT|CENTER)
        self.grid.addWidget(self.lab2,12,0,1,1)
        self.grid.addWidget(self.spinLente1,13,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.spinLente2,13,0,1,1,RIGHT|CENTER)

        self.lab = BodyLabel(("Periode de la ligne Signal :"))
        self.spinSignal = SpinBox((self.Widget))
        self.grid.addWidget(self.lab,14,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.spinSignal,14,0,1,1,RIGHT|CENTER)

        self.lab = BodyLabel(("Periode de la ligne %D :"))
        self.spinD = SpinBox((self.Widget))
        self.grid.addWidget(self.lab,15,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.spinD,15,0,1,1,RIGHT|CENTER)


        self.lab = BodyLabel(("Intervalle des donnees "))
        self.intervalle1 = SpinBox(self.Widget)
        self.intervalle2 = SpinBox(self.Widget)
        self.grid.addWidget(self.lab,16,0,1,2)
        self.grid.addWidget(self.intervalle1,17,0,1,1,LEFT|CENTER)
        self.grid.addWidget(self.intervalle2,17,0,1,1,RIGHT|CENTER)

        self.grid.setSpacing(10)
        self.spinRapide1.setValue(10)
        self.spinRapide2.setValue(25)
        self.spinLente1.setValue(15)
        self.spinLente2.setValue(45)
        self.spinSignal.setValue(4)
        self.spinD.setValue(4)


## NAvigation frame
        self.navigationFrame = QFrame(self)
        self.hBox = QHBoxLayout(self.navigationFrame)
        self.navigationFrame.setLayout(self.hBox)
        self.nexBtn= PushButton("Suivant", self.navigationFrame,qta.icon("ei.arrow-right"))
        self.hBox.addWidget(self.nexBtn, 0, RIGHT|CENTER)

        self.vBox = QVBoxLayout(self)
        self.setLayout(self.vBox)
        self.vBox.addWidget(self.scrollArea)
        self.vBox.addWidget(self.navigationFrame)        
        self.scrollArea.setWidget(self.Widget)
        self.scrollArea.setWidgetResizable(True)








class strategieResultatsInterface(QWidget) :
    def __init__(self , parent=None) :
        super().__init__(parent)

        self.Widget = QWidget(self)
        self.scrollArea = SmoothScrollArea(self)

## NAvigation frame
        self.navigationFrame = QFrame(self)
        self.hBox = QHBoxLayout(self.navigationFrame)
        self.navigationFrame.setLayout(self.hBox)
        self.nexBtn= PushButton("Suivant", self.navigationFrame,qta.icon("ei.arrow-right"))
        self.backBtn = PushButton("Precedent" , self.navigationFrame, qta.icon("ei.arrow-left"))
        self.hBox.addWidget(self.backBtn,0,LEFT|CENTER)
        self.hBox.addWidget(self.nexBtn,0,RIGHT|CENTER)

        self.strartBtn = PushButton("Commencer" , self , qta.icon("msc.debug-start"))
        self.textEd = TextEdit(self)
        self.imageLab = PixmapLabel(self)
        self.vBox2 = QVBoxLayout(self.Widget)

        self.vBox2.addWidget(self.textEd)
        self.vBox2.addWidget(self.imageLab)


        self.vBox = QVBoxLayout(self)
        self.setLayout(self.vBox)
        self.vBox.addWidget(self.strartBtn,0,LEFT|CENTER)
        self.vBox.addWidget(self.scrollArea)
        self.vBox.addWidget(self.navigationFrame)        
        self.scrollArea.setWidget(self.Widget)
        self.scrollArea.setWidgetResizable(True)


    def updateTextEdit(self, message):
        self.textEd.append(message)

    def LongprocessEd(self , data:dict) :
        self.process = Simulation(data )
        self.process.update_signal.connect(self.updateTextEdit)
        self.process.start()









class databaseInterface(QWidget) :
    def __init__(self , parent=None) :
        super().__init__(parent)

        self.Widget = QWidget(self)
        self.scrollArea = SmoothScrollArea(self)

## NAvigation frame
        self.navigationFrame = QFrame(self)
        self.hBox = QHBoxLayout(self.navigationFrame)
        self.navigationFrame.setLayout(self.hBox)
        self.backBtn = PushButton("Precedent" , self.navigationFrame, qta.icon("ei.arrow-left"))
        self.hBox.addWidget(self.backBtn,0,LEFT|CENTER)

## Haed frame 
        self.headFrame = QFrame(self)
        self.hbox = QHBoxLayout(self.headFrame)
        self.lineEd = LineEdit(self.headFrame)
        self.printBtn = PushButton(" ",self.headFrame,qta.icon("mdi6.printer-pos"))
        self.seachBtn = PushButton(" ",self.headFrame,qta.icon("fa.search"))
        self.hbox.addWidget(self.lineEd,1)
        self.hbox.addWidget(self.printBtn)
        self.hbox.addWidget(self.seachBtn)
        self.lineEd.setPlaceholderText("exemple : Rapide>9   and   Lente>=19  or   PositiveP>=90 ")

## Table Wdget
        self.tableWidget = TableWidget(self.Widget)

## adding Widget 
        self.vBox = QVBoxLayout(self)
        self.setLayout(self.vBox)
        self.vBox.addWidget(self.headFrame)
        self.vBox.addWidget(self.scrollArea)
        self.vBox.addWidget(self.navigationFrame)        
        self.scrollArea.setWidget(self.Widget)
        self.scrollArea.setWidgetResizable(True)
        self.hBoxW = QHBoxLayout(self.Widget)
        self.hBoxW.addWidget(self.tableWidget)

        self.process = None
        self.process2 = None
        self.printBtn.clicked.connect(self.LongProcess) 
        self.seachBtn.clicked.connect(self.longPrcess2)
        self.lineEd.setPlaceholderText("exemple : Rapide>9   and   Lente>=19  or   PositiveP>=90 ")
    
    def updateTable(self,message) :
        self.tableWidget.update()

    
    def LongProcess(self) :
        if self.process is None or self.process.isFinished()==True:
            self.process = tableWidgetThread(table=self.tableWidget,btn=self.lineEd )
            self.process.update_signal.connect(self.updateTable)
            self.process.start()

    def longPrcess2(self) :
        if self.process2 is None:
            self.process2 = tableWidgetQueryThread(self.tableWidget , self.lineEd )
            self.process2.update_signal.connect(self.updateTable)
            try:
                self.process2.start()
            except Exception as e : print(e)
        else :
            self.process2.update_signal.connect(self.updateTable)
            self.process2.start()

class Stoch(QStackedWidget) :
    def __init__(self , parent=None):
        super().__init__(parent)

## GEt DAta base Interface
        self.getDataInterface = getDataInterface(self)
        self.addWidget(self.getDataInterface)

## GEt Strategie Information 
        self.getInfoInterface = getStrategiInfosInterface(self)
        self.addWidget(self.getInfoInterface)

## Interface Resultats
        self.resultInterface = strategieResultatsInterface(self)
        self.addWidget(self.resultInterface)

## DAtaBase Interface
        self.databaseInterface = databaseInterface(self)
        self.addWidget(self.databaseInterface)

        self.setCurrentWidget(self.getDataInterface)
        #self.getDataInterface.nextBtn.setEnabled(True)
        self.initButton()

    def initButton(self) :
        self.getDataInterface.nextBtn.clicked.connect(lambda : self.setCurrentWidget(self.getInfoInterface) )
        self.getDataInterface.nextBtn.clicked.connect(lambda: self.initObject() )

        self.getInfoInterface.nexBtn.clicked.connect(lambda : self.setCurrentWidget(self.resultInterface))
        self.resultInterface.nexBtn.clicked.connect(lambda : self.setCurrentWidget(self.databaseInterface))
        
        self.resultInterface.backBtn.clicked.connect(lambda : self.setCurrentWidget(self.getInfoInterface))
        self.databaseInterface.backBtn.clicked.connect(lambda : self.setCurrentWidget(self.resultInterface))

        self.resultInterface.strartBtn.clicked.connect(self.initparametre)
        self.resultInterface.strartBtn.clicked.connect(lambda : self.resultInterface.LongprocessEd(data=self.data))


    def initObject(self) :
        df = read_csv(self.getDataInterface.filePath)
        column = df.columns.to_list()
        
        for c in column :
            if str(df[c].dtype) == "object" :
                self.getInfoInterface.combo1.addItem(c)
            
            elif str(df[c].dtype)==("float64" or "int64") :
                self.getInfoInterface.combo2.addItem(c)
                self.getInfoInterface.combo3.addItem(c)
                self.getInfoInterface.combo4.addItem(c)

        self.getInfoInterface.intervalle1.setMaximum(len(df)-10)
        self.getInfoInterface.intervalle2.setMaximum(len(df))
        self.getInfoInterface.intervalle1.setValue(len(df)-50)
        self.getInfoInterface.intervalle2.setValue(len(df))


    def initparametre(self) :
        filename= self.getDataInterface.filePath
        indexCol = self.getInfoInterface.combo1.currentText()
        df = read_csv(filename,index_col=indexCol)
        rapide = [self.getInfoInterface.spinRapide1.value() , self.getInfoInterface.spinRapide2.value()]
        lente = [self.getInfoInterface.spinLente1.value(), self.getInfoInterface.spinLente2.value() ]
        niveau = self.getInfoInterface.spinD.value()
        signal = self.getInfoInterface.spinSignal.value()
        close = self.getInfoInterface.combo2.currentText()
        hight = self.getInfoInterface.combo3.currentText()
        low = self.getInfoInterface.combo4.currentText()

        self.data = {
            "df":df,
            "index":indexCol,
            "rapide":rapide,
            "lente":lente,
            "niveau":niveau,
            "signal":signal,
            "close":close,
            "low":low,
            "hight":hight
        }




class Simulation(QThread) :
    update_signal  = pyqtSignal(str)

    def __init__(self ,data:dict) :
        super().__init__()
        self.data = data
        
        self.rapide = self.data["rapide"]
        self.lente = self.data["lente"]


    def run(self) :
        Data = {
            "📎":[],
            "rapide":[],
            "lente":[],
            "niveau":[],
            "signal":[],
            "positive":[],
            "negative":[],
            "benefice":[],
        }

        for i in range(10) :
            for rapide in range(self.rapide[0], self.rapide[1]) :
                for lente in range(self.lente[0], self.lente[1] ):
                    if lente >= (rapide)+2 :

                        strategie = OS_MACD(
                            df=self.data['df'],
                            rapide=rapide,
                            lente=lente,
                            niveau=self.data["niveau"],
                            signal=self.data["signal"],
                            close=self.data['close'],
                            low=self.data['low'],
                            hight=self.data['hight']
                        )

                        if strategie.pourcentage_benefice <20 :
                            message= f"Parametres ({rapide} , {lente} , {self.data['niveau']} , {self.data['signal']}) "
                            message+=f"Transaction positive : {strategie.positive} "
                            message+=f"Transaction negative : {strategie.negative}  "
                            message+=f"Poucentage benefice : {strategie.pourcentage_benefice} %  ❗❗\n"
                            Data["📎"].append("❗")
                        else :
                            message= f"Parametres ({rapide} , {lente} , {self.data['niveau']} , {self.data['signal']})  "
                            message+=f"Transaction positive : {strategie.positive} "
                            message+=f"Transaction negative : {strategie.negative} "
                            message+=f"Poucentage benefice : {strategie.pourcentage_benefice} %  ✅✅\n"
                            Data["📎"].append("✅")

                        Data["rapide"].append(rapide)
                        Data["lente"].append(lente)
                        Data["niveau"].append(self.data["niveau"])
                        Data["signal"].append(self.data["signal"])
                        Data["positive"].append(strategie.positive)
                        Data["negative"].append(strategie.negative)
                        Data["benefice"].append(strategie.pourcentage_benefice)

                        self.update_signal.emit(message)
                        self.msleep(100)

        df = DataFrame(Data)
        df.to_csv(r"db/OS_DATABASE.csv")
        conn = sql.connect("db/OS_DATABASE.db")
        df.to_sql(name="resultats" , con=conn,if_exists="replace",index=False)


class tableWidgetThread(QThread) :
    update_signal = pyqtSignal(dict)
    
    def __init__(self , table:TableWidget , btn:LineEditButton) -> None:
        super().__init__()
        self.df = read_csv("db/OS_DATABASE.csv",index_col=0)
        self.table = table
        self.btn = btn
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(list(self.df.columns))
        
    def run(self) :
        t=self.table.rowCount()
        self.btn.setEnabled(False)
        for k in range(t) :
            self.table.removeRow(0)
            self.update_signal.emit({3:3})
            self.msleep(1)
        
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
        self.btn.setEnabled(True)
        #self.update_signal.emit({"i":i,"len":taille,"data":self.df.iloc[i]})
    
 
class tableWidgetQueryThread(QThread) :
    update_signal = pyqtSignal(dict)
    
    def __init__(self , table:TableWidget ,lineEd:LineEdit) -> None:
        super().__init__()
        self.conn = sql.connect("db/OS_DATABASE.db")
        self.df0 = read_sql("SELECT * FROM resultats",self.conn)
        self.table = table
        
        self.lineEd = lineEd
        self.table.setColumnCount(len(self.df0.columns))
        self.table.setHorizontalHeaderLabels(list(self.df0.columns))
        
    def run(self) :
        try :
            self.query = self.lineEd.text()
            print("la requete : " , self.query)
            #self.conn = sql.connect("db/MA_DATABASE.db")
            #self.df0 = read_sql("SELECT * FROM resultats",self.conn)
            self.dff = self.df0.query(self.query)
            t=self.table.rowCount()
            for k in range(t) :
                self.table.removeRow(0)
                self.update_signal.emit({3:3})
                self.msleep(1)
            
            taille = len(self.dff)
            colTaiile = len(self.dff.iloc[1])
            for i in range(len(self.dff )) :
                self.table.insertRow(i)    
                self.table.selectRow(i)        
                for j in range(len(self.dff.iloc[i])) :
                    self.table.setItem(i,j,QTableWidgetItem(str(self.dff.iloc[i][j])))
                    self.update_signal.emit({1:3})
                    self.msleep(1)
            self.table.selectRow(0)
            #self.update_signal.emit({"i":i,"len":taille,"data":self.df.iloc[i]})
        except Exception as e : print(e)