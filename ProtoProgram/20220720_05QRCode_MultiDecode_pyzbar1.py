import code
from pyzbar.pyzbar import decode
import cv2

def own_decoder(frame):
    from PIL import Image
    pil_image = Image.fromarray(frame)
    barcodes = decode(pil_image)
    for barcode in barcodes:
        return barcode

def real_time_qrcode_detection():
    import cv2
    cap = cv2.VideoCapture(0)     # 自行設定

    strcheck = ""      # 先假定一個空字串
    while True:
        ret, frame = cap.read()
        barcode = own_decoder(frame)
        if barcode:
            x, y, w, h = barcode.rect
            message = barcode.data
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(frame, message.decode(), (x,y), font, 3, (255, 20, 255), 5)
            # print(barcode)    # 可以看到所有QRCode的內容
            codedata = barcode.data.decode('utf-8')    # 僅顯示data內容並用utf-8解碼字體
            # codedata = decode('ascii')
            if strcheck != codedata:  # 當空字串不等於內容時
                strcheck = codedata     # 空字串會等於內容
                print(codedata)           #打印出來

        # frame = cv2.resize(frame, (600, 540))
        cv2.imshow('decoder window', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    real_time_qrcode_detection()
    # create_barcode('barcode.png')
    # decode_and_detect_barcode('barcode.png')