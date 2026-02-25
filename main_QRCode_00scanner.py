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
    return barcodes

def real_time_qrcode_detection():
    decoded_list = []
    ret, frame = cap.read()
    if not ret:
        return decoded_list
    barcodes = own_decoder(frame)
    # frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        message = barcode.data
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        try:
            # Try to decode data for display, handle errors
            display_text = message.decode('utf-8', errors='replace')
            cv2.putText(frame, display_text[:20], (x,y), font, 1, (255, 20, 255), 2)
            decoded_list.append(display_text)
        except Exception as e:
            print(f"Decode error: {e}")

    cv2.imshow('decoder window', frame)
    return decoded_list

def QRCodedata():
    while True:
        codedata_list = real_time_qrcode_detection()
        var.QRCodeList = codedata_list
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        # sleep(0.1)    # 可以不用一直掃描

    cap.release()
    cv2.destroyAllWindows()

# if __name__ == '__main__':          # for run test
#     QRCodedata()
