from .lib import *
from qfluentwidgets import BodyLabel
import qtawesome  as qta



class ScrollAr(SmoothScrollArea) :
    def __init__(self, parent=None):
        super().__init__(parent)


class TraitementInterface(QWidget) :
    def __init__(self , parent: QStackedWidget=None):
        super().__init__(parent)
        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)

        self.scrollArea = ScrollAr(self)
        self.scrollArea_Widget = QWidget(self.scrollArea)
        self.vBox.addWidget(self.scrollArea)

        self.vbox2 = QVBoxLayout(self.scrollArea_Widget)
        self.scrollArea_Widget.setLayout(self.vbox2)

        self.getfileBtn = PushButton("Cliquer",self.scrollArea_Widget,FIF.DOWNLOAD)
        self.filenameLab = BodyLabel(self.scrollArea_Widget)
        
        self.frame = QFrame(self.scrollArea_Widget)
        self.hbox = QHBoxLayout(self.frame)
        self.hbox.addWidget(self.getfileBtn,0,LEFT|CENTER)
        self.hbox.addWidget(self.filenameLab,1,LEFT|CENTER)
        
        self.frame2 = QFrame(self.scrollArea_Widget)
        self.hbox = QHBoxLayout(self.frame2)
        self.combo1 = ComboBox(self.frame2)
        self.combo2 = ComboBox(self.frame2)
        self.lab1 = BodyLabel(self.frame2)
        self.lab1.setText("Variables : ")
        self.lab2 = BodyLabel(self.frame2)
        self.lab2.setText("Convertir en : ")
        self.lab3 = BodyLabel(self.frame2)
        self.line1= LineEdit(self.frame2)
        self.lab4 = BodyLabel(self.frame2)
        self.lab4.setText("par")
        self.line2= LineEdit(self.frame2)
        self.message = CaptionLabel(self.frame2)
        self.convertBtn = PushButton(self.scrollArea_Widget)

        self.combo2.addItems(["str",
        "int","float","Supprimer la Virgule" , 
        "round(1)", "round(2)","Remplacer 'abc' par 'fg' "])
        self.line1.setPlaceholderText("abc")
        self.line2.setPlaceholderText("ef")
        self.convertBtn.setText("Convertir la colonne ")
        self.saveData = PushButton(self.scrollArea_Widget)
        self.saveData.setText("Enregister la base de donnees")

        self.hbox.addWidget(self.lab1,0,LEFT|CENTER)
        self.hbox.addWidget(self.combo1,0,LEFT|CENTER)
        self.hbox.addWidget(self.lab3,0,LEFT|CENTER)
        self.hbox.addWidget(self.lab2,0,LEFT|CENTER)
        self.hbox.addWidget(self.combo2,0,LEFT|CENTER)
        self.hbox.setSpacing(0)
        self.hbox.addWidget(self.line1,0,LEFT|CENTER)
        self.hbox.addWidget(self.lab4,0,LEFT|CENTER)
        self.hbox.addWidget(self.line2,0,LEFT|CENTER)


        ## table Widget
        self.tableWidget = TableWidget(self.scrollArea_Widget)


        ## Adding widget 
        self.vbox2.addWidget(self.frame)
        self.vbox2.addWidget(self.frame2)
        self.vbox2.addWidget(self.message)
        self.vbox2.addWidget(self.convertBtn)
        self.vbox2.addWidget(self.tableWidget)
        self.vbox2.addWidget(self.saveData)
        self.scrollArea.setWidget(self.scrollArea_Widget)
        self.scrollArea.setWidgetResizable(True)
        
        self.process = None
        self.frame2.setHidden(True)
        self.convertBtn.setHidden(True)
        self.saveData.setHidden(True)
        self.initButton()
    
    def changeColum(self):
        col = self.combo1.currentText()
        type_ = self.combo2.currentText()

        if type_=="str" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : str(x) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "int" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : int(x) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "float" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : float(x) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "round(1)" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : round(x,1) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "round(2)" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : round(x,2) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "Supprimer la Virgule" :
            try : 
                self.process.df[col] = self.process.df[col].apply(lambda x : str(x).replace(",",".") )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))
        elif type_== "Remplacer 'abc' par 'fg' " :
            try : 
                a = self.line1.text() ; b = self.line2.text()
                self.process.df[col] = self.process.df[col].apply(lambda x : str(x).replace(a , b) )
                self.process.start()
            except Exception  as e : self.message.setText(str(e))

    def show_save_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Enregistrer le fichier', '', 'Fichiers CSV (*.csv)', options=options)
        print(file_name)
        self.process.df.to_csv(file_name)


    def initButton(self) :
        self.getfileBtn.clicked.connect(self.fileDialog)
        self.getfileBtn.clicked.connect(self.long_process)
        self.combo1.currentTextChanged.connect(self.comboUpdate)
        self.convertBtn.clicked.connect(self.changeColum)
        self.saveData.clicked.connect(self.show_save_dialog)


    def fileDialog(self) :
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;XLSX (*.xlsx)")
        self.filenameLab.setText(f"Fichier : {self.filePath}")
        if self.filePath :
            self.frame2.setHidden(False)
            self.convertBtn.setHidden(False)
            self.saveData.setHidden(False)
        else :
            self.frame2.setHidden(True)
            self.convertBtn.setHidden(True)
            self.saveData.setHidden(True)


    def updateTable(self,message) :
        self.tableWidget.update()        
    
    def convertColums(self) :
        pass

    def long_process(self) :
        if self.filePath : 
            if self.process is None : 
                self.process = tableWidgetThread(table=self.tableWidget,
                            filename=self.filePath,btn=self.getfileBtn)
                self.process.update_signal.connect(self.updateTable)
                self.process.start()
            else :
                self.process.__init__(table=self.tableWidget,
                            filename=self.filePath,btn=self.getfileBtn)
                self.process.start()

            for i in range(self.combo1.count()) :
                self.combo1.removeItem(i)

            self.combo1.addItems(self.process.columnList)

    def comboUpdate(self,text) :
        self.lab3.setText(self.process.columnTypes[self.combo1.currentIndex()])
        self.lab3.update()

class tableWidgetThread(QThread) :
    update_signal = pyqtSignal(dict)

    def __init__(self, table:TableWidget , filename:str,btn:PushButton) :
        super().__init__()
        self.table = table
        self.filename = filename
        self.btn = btn

        self.df = read_csv(self.filename)
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(list(self.df.columns))
        self.columnList = self.df.columns.to_list()


    def run(self) :
        self.columnList = self.df.columns.to_list()
        self.columnTypes = [ str(self.df[col].dtype) for col in self.columnList  ]

        t=self.table.rowCount()
        self.btn.setEnabled(False)
        for k in range(t) :
            self.table.removeRow(0)
            self.update_signal.emit({3:3})
            self.msleep(1)
        
        taille = len(self.df)
        colTaiile = len(self.df.iloc[1])
        if taille <=300 :
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
        else :
            for i in range(len(self.df )) :
                self.table.insertRow(i)    
                self.table.selectRow(i)        
                for j in range(len(self.df.iloc[i])) :
                    self.table.setItem(i,j,QTableWidgetItem(str(self.df.iloc[i][j])))
                
            self.table.selectRow(0)
            self.update_signal.emit({1:3})
            self.btn.setEnabled(True)
            #self.update_signal.emit({"i":i,"len":taille,"data":self.df.iloc[i]})
        
 