import sys
import iconify as ico
from PySide2 import QtGui
from win32api import GetSystemMetrics 
from PIL import Image , ImageFilter
import pyautogui
from time import sleep

WIDTH_ = GetSystemMetrics(0) 
HEIGHT_ = GetSystemMetrics(1) 
img_ = 'images/bg.jpg'
img = Image.open("images/image6.jpg")
img = Image.eval(img , lambda x: x/1)
img = img.filter(ImageFilter.GaussianBlur(radius=3))
img = img.resize((WIDTH_,HEIGHT_)).save(img_)


USAGE_LIST = ['Hotel de tourisme','Hotels de séjour','Foyers de jeunes travailleurs',
                        'Bureau','Maison de retraite','Foyer de personne âgées',
                        'Hôtels de sports d\'hiver','Hôtels à clientèle spécifique',
                        "Cantines","Restaurents","Sanitaires publics","Ecoles","Internats",
                        "Stades","Gymnases","Casernes"]

TRONCON = ['Canalisation en sous-sol', "Colonne montante"]

CATEGORIE = ['Plastique','Cuivre','Acier galvaniser']

APPAREIL_LIST = ["01. Evier,timbre d'office",
        "02. Lavabo",
        "03. Lavabo collectif (par jet)",
        "04. Bidet",
        "05. Baignoire",
        "06. Douche ",
        "07. Poste d eau robinet 1/2",
        "08. Poste d'eau robinet 3/4","09. WC avec recervoir de chasse",
        "10. WC avec robinet de chasse" ,
        "11. Urinoir avec robinet individuel"  ,
        "12. Lave-main" ,
        "13. Bac a laver",
        "14. Machine à laver le linge",
        "15. Machine à laver la verselle"
        ]


scrollStyle = """
        QWidget{background-color: transparent ;}
        QLabel,QPushButton,QSpinBox,QDoubleSpinBox,QComboBox{font : 13pt; text-align: center
        ;background-color:rgba(200,200,200,0.5)}
        QGridLayout{padding-left:50}
        """