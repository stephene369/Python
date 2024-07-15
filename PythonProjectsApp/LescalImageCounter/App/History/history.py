from ..Lib  import * 
from ..Class import Widget

class HistoryInterface(Widget) :
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)

        self.HistoryScrollArea = SingleDirectionScrollArea(self)

        self.historyWidget = HistoryWidget(self.HistoryScrollArea)

        self.vBox = QVBoxLayout(self)
        self.vBox.addWidget(self.HistoryScrollArea)
        
        self.HistoryScrollArea.setWidget(self.historyWidget)
        self.HistoryScrollArea.setWidgetResizable(True)
        
        self.setContentsMargins(0,0,0,0)
        self.HistoryScrollArea.setContentsMargins(0,0,0,0)
        self.vBox.setContentsMargins(0,30,0,0)



class HistoryWidget(QWidget) :
    def __init__(self , parent) :
        super().__init__(parent=parent)

        self.VBox = QVBoxLayout(self)
        try :
            with open("History\history.json","r" ) as js :
                data = json.load(js)
            
            for i in range(len(data[1])) :
                try :
                    widget = HistoryCard(
                        image=data[1][i]["image"],
                        image_=data[1][i]["image-counted"],
                        nombre=data[1][i]["count"]
                    )
                    self.VBox.addWidget(widget)
                except Exception as e : print("Exception : ",e  )
        except Exception as e : print(e)

class HistoryCard(CardWidget) :
    def __init__(self,image:str,image_:str,nombre:int,parent=None):
        super().__init__(parent )

        #self.imageLabel = ImageLabel(self)
        self.imageCountedLabel = ImageLabel(self)
        self.numberLabel = TitleLabel(self)

        #self.imageLabel.setImage(image)
        self.imageCountedLabel.setImage(image_)
        self.numberLabel.setText("Élements : "+str(nombre))

        #self.caption0 = CaptionLabel(self)
        self.caption1 = CaptionLabel(self)

        #self.caption0.setText("original")
        self.caption1.setText("counted")

        self.HBOX = QHBoxLayout(self)
        
        #self.vBox0 = QVBoxLayout()
        #self.vBox0.addWidget(self.imageLabel,0,CENTER)
        #self.vBox0.addWidget(self.caption0,0,CENTER)

        self.vBox1 = QVBoxLayout()
        self.vBox1.addWidget(self.imageCountedLabel,0,LEFT|CENTER)
        self.vBox1.addWidget(self.caption1,0,CENTER)

        self.HBOX.addWidget(self.numberLabel,0,CENTER)
        self.HBOX.setAlignment(LEFT|CENTER)
        self.HBOX.addLayout(self.vBox1,1)
        #self.HBOX.addLayout(self.vBox0)
        
    