from multiprocessing.sharedctypes import Value
from time import sleep
from pyzbar.pyzbar import decode
import cv2
from PIL import Image
import main_Global_Var as var

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)     # CAP_DSHOW處理WARN global問題

def own_decoder(frame):
    #from PIL import Image
    pil_image = Image.fromarray(frame)
    barcodes = decode(pil_image, symbols=[64])  # symbols=[64]處理 WARNING: .\zbar\decoder\pdf417.c:73的問題
    for barcode in barcodes:
        return barcode

def real_time_qrcode_detection():
    strcheck = ""      # 先假定一個空字串
    ret, frame = cap.read()
    barcode = own_decoder(frame)
    # frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    if barcode:
        x, y, w, h = barcode.rect
        message = barcode.data
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, message.decode(), (x,y), font, 3, (255, 20, 255), 5)
        # print(barcode)    # 可以看到所有QRCode的內容
        # 僅顯示data內容並用utf-8解碼字體
        strcheck = barcode.data.decode('utf-8')
        print(barcode.data)
    cv2.imshow('decoder window', frame)
    return strcheck

def QRCodedata():
    while True:
        codedata = real_time_qrcode_detection()
        # if codedata != "" and var.QRCodeStr != codedata:
        var.QRCodeStr = codedata
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        # sleep(0.1)    # 可以不用一直掃描

    cap.release()
    cv2.destroyAllWindows()

# if __name__ == '__main__':          # for run test
    # QRCodedata
