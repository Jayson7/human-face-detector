import cv2
human_c = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, img =cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = human_c.detectMultiScale(gray, 1.1, 4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k ==27:
            break
cap.realease()