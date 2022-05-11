import cv2
import winsound
c = cv2.VideoCapture(0)                                                             # Number of your camera default is 0
while c.isOpened():
    r, fra1 = c.read()                                                                               # reading and frame
    r, fra2 = c.read()
    d = cv2.absdiff(fra1, fra2)
    gray = cv2.cvtColor(d, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    di = cv2.dilate(thresh, None, iterations=4)
    con, _ = cv2.findContours(di, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(fra1, con, -1, (0, 255, 0), 2)
    for c in con:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(fra1, (x, y), (x+w, y+w), (0, 255, 0), 2)
        winsound.Beep(500, 200)
        winsound.PlaySound('soundsong.wav', winsound)
    if cv2.waitKey(10) == ord('Q'):
        break
    cv2.imshow("Solar robo Camera", fra1)                                                         # pop up message



