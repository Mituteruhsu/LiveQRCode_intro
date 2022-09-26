import cv2

cap = cv2.VideoCapture(0) # Webcame鏡頭的編號，0 內建鏡頭，1 外接鏡頭

while(True):
    _, frame = cap.read()
    if _:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(15) == ord('q'): # ord按q就直接停止
        break