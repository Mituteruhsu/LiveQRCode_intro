from time import sleep
import cv2
from PIL import Image
import numpy as np

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)     # CAP_DSHOW處理WARN global問題
qrcode = cv2.QRCodeDetector()

def own_decoder(frame):
    #from PIL import Image
    # pil_image = Image.fromarray(frame)
    ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(frame)
    return ok, data, bbox

def real_time_qrcode_detection():
    strcheck = ""      # 先假定一個空字串
    ret, frame = cap.read()
    ok, data, points = own_decoder(frame)
    # frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    if ok:
        message = data
        x=(np.int32(points)[0][0][0])
        y=(np.int32(points)[0][0][1])
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.polylines(frame, [np.int32(points)], True, (255, 255, 0), 4)
        cv2.putText(frame, message, (x,y), font, 3, (255, 20, 255), 5)
        # print(barcode)    # 可以看到所有QRCode的內容
        # 僅顯示data內容並用utf-8解碼字體
        strcheck = message
    cv2.imshow('decoder window', frame)
    return strcheck

def QRCodedata():
    strcheck = ""
    while True:
        codedata = real_time_qrcode_detection()
        if codedata != "" and strcheck != codedata:
            strcheck = codedata
            print(codedata)
        key = cv2.waitKey(1)
        if key == 27:
            break
        # sleep(0.1)    # 可以不用一直掃描

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    QRCodedata()
    
