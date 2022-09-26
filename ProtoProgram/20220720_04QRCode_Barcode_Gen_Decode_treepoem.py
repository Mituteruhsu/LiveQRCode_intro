from pyzbar.pyzbar import decode
import treepoem
import cv2


def create_barcode(filename):
    image = treepoem.generate_barcode(
        barcode_type = 'code128',
        data = '1245789363'
    )
    image.covert('1').svae(filename)


def decode_and_detect_barcode(filename):
    image = cv2.imread(filename)
    barcodes = decode(image)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 10, 100), 2)
        print(barcode.data)
    cv2.imshow('barcode window', image)
    cv2.waitKey(0)


def own_decoder(frame):
    from PIL import Image
    pil_image = Image.fromarray(frame)
    barcodes = decode(pil_image)
    for barcode in barcodes:
        return barcode


def real_time_qrcode_detection():
    import cv2
    cap = cv2.VideoCapture(0)     # 自行設定
    while True:
        ret, frame = cap.read()
        barcode = own_decoder(frame)
        if barcode:
            print(barcode)
            x, y, w, h = barcode.rect
            message = barcode.data
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(frame, message.decode(), (x,y), font, 3, (255, 20, 255), 5)
        frame = cv2.resize(frame, (600, 540))
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