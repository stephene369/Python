from Ui.library import *
from modules.MatPlot import *
from modules.maModul import getParameter

class Page2_1 :
    def __init__(self , parent:QWidget , dbName:str):
        self.dbName = dbName
        self.parent = parent 
        self.ScrollArea = QScrollArea(self.parent)
        self.page = QWidget(self.ScrollArea)

        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setWidget(self.page)
        self.VBOX = QVBoxLayout(self.page)
        self.page.setLayout(self.VBOX)

    def setupUi(self ):
        self.rapide = [OBJECT['courte'][0].value() , OBJECT['courte'][1].value()  ]
        self.lente = [OBJECT['longue'][0].value() , OBJECT['longue'][1].value() ]

### FRAME 1 : IMAGE DE LA TENDANCE DE L'HORIZON TEMPOREL
        self.frame1 = QFrame(self.page)
        self.tendanceView = QLabel(self.frame1)

        QVBoxLayout(self.frame1).addWidget(self.tendanceView)

## LAYOUT PRINCIPAL 
        self.VBOX.addWidget(self.frame1)

## STYLE SCHET
        with open("style/maResult.scss") as sc :
            self.page.setStyleSheet(sc.read())

## MATPLOTLIB FIGURE
        self.Plt_tendance = plt
        self.Plt_tendance.figure( figsize=(12,7) )
        

        return self.ScrollArea
    
    def plotTendance(self) :

        #img=Image.open("images/tendance.png").resize(self.tendanceView.size().toTuple()  )
        #img.save("images/tendance.png")
        
        img = QPixmap("images/tendance.png")
        
        self.tendanceView.setPixmap(img)
        

    def creeTendance(self) :
        tendance = OBJECT["horizon"].currentText()
        self.df = read_csv(self.dbName,index_col="Date")
        self.df = self.df[-300:]

        self.getParameter = getParameter()
        self.parametre = self.getParameter.parameter()

        self.Plt_tendance.plot(self.df.index, 
        self.df["Close"].values, linewidth = 1 
        , label = f"Cours de la valeur" )
        
        self.Plt_tendance.plot(self.df.index, 
        self.df["Close"].rolling(self.parametre[0]).mean() , 
        linewidth = 1, label = f"MA{self.parametre[1]}" )
        
        self.Plt_tendance.plot(self.df.index, 
        self.df["Close"].rolling(self.parametre[1]).mean(), 
        linewidth = 1 , label = f"MA{self.parametre[1]}" )

        self.x_tick_id = [int(i) for i in linspace(0 , len(self.df) , 10 )] 
        self.x_tick_val = [self.df.iloc[i].name for i in self.x_tick_id[:-1] ]

        
        self.Plt_tendance.xticks( self.x_tick_id[:-1] , self.x_tick_val , rotation=0 )
        self.Plt_tendance.title(f"Tendance à {tendance}" )
        self.Plt_tendance.legend()
        self.Plt_tendance.tight_layout()
        self.Plt_tendance.savefig("images/tendance.png")


    def para(self) :
        thread = Thread(target=self.creeTendance)
        thread.start()
        thread.join()
        

        thread = Thread(target=self.plotTendance)
        thread.start()

