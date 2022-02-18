from cv2 import cv2
import time
import os
import hand as htm

cap=cv2.VideoCapture(0)

sTime = 0
FolderPath ="Fingers"

lst = os.listdir(FolderPath)
lst_img =[]
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    lst_img.append(image)


detector = htm.handDetector(detectionCon=0.55)
while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw=False)
    print(lmList)

    #print image finger
    h, w, c = lst_img[0].shape
    frame[0:h, 0:w] = lst_img[0]

    #print fps
    fTime = time.time()
    fps = 1/(fTime-sTime)
    
    sTime = fTime
    cv2.putText(frame,f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    
    cv2.imshow("Viet Viet",frame)
    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()