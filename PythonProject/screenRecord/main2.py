import pyautogui
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication , QLineEdit , QWidget , QHBoxLayout
import sys
import threading

filename = "Recording.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0
resolution = (1920, 1080)
out = cv2.VideoWriter(filename, codec, fps, resolution)

app = QApplication(sys.argv)
window = QWidget()
hbox = QHBoxLayout(window)
line = QLineEdit(window)


def record() :
    while True:
        img = pyautogui.screenshot()

        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        out.write(frame)
        #cv2.imshow('Live', frame)

        window_state = cv2.getWindowProperty('Live', cv2.WND_PROP_VISIBLE)
        if line.text() =='q' :    break
        #if cv2.waitKey(1) == -14:#ord('q'): break

tread = threading.Thread( target=record )

window.show()

tread.start()

out.release()
cv2.destroyAllWindows()

sys.exit(app.exec())