from cv2 import cv2
import time
import os


FolderPath="Fingers"
lst=os.listdir(FolderPath)
print(lst)
lst_2=[]  
for i in lst:
    #print(i)
    image=cv2.imread(f"{FolderPath}/{i}")   
    #print(f"{FolderPath}/{i}")
    lst_2.append(image)
print(len(lst_2))
pTime=0

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    h, w, c = lst_2[0].shape
    frame[0:h,0:w] = lst_2[0]


    cv2.imshow("Sign language test",frame)

    if cv2.waitKey(1) == ord("q"):
        break
 
cap.release()
cv2.destroyAllWindows()