from datetime import datetime
from PySide2.QtWidgets import QLabel 
from PySide2.QtCore import Qt, QTimer
import time

def dateheure( x : str) :
    date_heure = datetime.now()
    if x == 'date' :
        return date_heure.strftime('%d/%m/%Y')
    elif x == 'heure' :
        return date_heure.strftime('%H:%M')
    else :
        return 0


def pupdate_time(label : QLabel ):
    current_time = time.strftime("%I:%M:%S %p")  # Obtenir l'heure actuelle au format HH:MM:SS AM/PM
    label.setText(current_time)  # Mettre à jour le texte de l'étiquette avec l'heure actuelle

def setdateheure(heurelab : QLabel , datelab = QLabel) :
    datelab.setText(dateheure('date'))
    timer = QTimer()
    timer.timeout.connect(pupdate_time(heurelab))
    timer.start(1000) 
