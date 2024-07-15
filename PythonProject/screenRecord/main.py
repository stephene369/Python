import pyautogui
import cv2
import numpy as np

filename = "Recording.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 10.0
resolution = (1920, 1080)

out = cv2.VideoWriter(filename, codec, fps, resolution)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    out.write(frame)
    #cv2.imshow('Live', frame)

    window_state = cv2.getWindowProperty('Live', cv2.WND_PROP_VISIBLE)
    if window_state == 1.0 :break
    #if cv2.waitKey(1) == -14:#ord('q'): break

out.release()
cv2.destroyAllWindows()

