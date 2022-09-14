from pyzbar.pyzbar import decode
import cv2
from PIL import Image
import numpy as np
from time import sleep

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)     # CAP_DSHOW處理WARN global問題

def pyzbarDeco():
    pybarcode = ""
    ret, frame = cap.read()
    pil_image = Image.fromarray(frame)
    barcodes = decode(pil_image, symbols=[64])  # symbols=[64]處理 WARNING: .\zbar\decoder\pdf417.c:73的問題
    # print('======Here=======')
    # print(type(barcodes), barcodes)
    for barcode in barcodes:
        if barcode:
            x, y, w, h = barcode.rect
            pyptx=(x,y)
            pypty=(x+w, y+h)
            pymessage = barcode.data
            pypts = np.array([barcode.polygon],np.int32)
            pybarcode=barcode.data.decode('utf-8')
            font = cv2.FONT_HERSHEY_DUPLEX
            print('------------ex1:-------------------')
            print(type(barcode.rect), barcode.rect)
            print(type(barcode.polygon), barcode.polygon)
            print(f'pyptx:{pyptx}')
            print(f'pypty:{pypty}')
            print(f'pymessage:{pymessage}')
            print(f'pymessage:{pybarcode}')
            print(f'pypts:{pypts}')
            sleep(0.01)
            # cv2.rectangle(frame, pyptx, pypty, (0,0,255), 5)  # 繪製外框box[0],box[3]
            cv2.polylines(frame, [pypts], True, (0, 255, 0), 4)
            # cv2.putText(frame, pymessage, pyptx, font, 3, (0, 0, 255), 5) # 顯示文字
            
    cv2.imshow('decoder window', frame)
    return pybarcode

def QRCodedata():
    while True:
        codedata = pyzbarDeco()
        QRCodestr=""
        if codedata != "" and QRCodestr != codedata:
            QRCodestr = codedata
            # print(type(QRCodestr),'from pyzbar: ', QRCodestr)
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        # sleep(0.1)    # 可以不用一直掃描

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':          # for run test
    QRCodedata()